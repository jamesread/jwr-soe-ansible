# podman_app

Runs any container image as a systemd service, using a [Podman quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html).
This is the approved way to deploy podman apps in this collection.

Writes `<podman_app_name>.container` (and a `.network` per network), plus any
config files, and restarts the service only when one of those, or the image,
changes. Apps start at boot. Requires podman 4.4 or newer, and 5.0 or newer
for healthchecks.

Common apps have their own wrapper roles with sensible defaults, eg
[podman_app_prometheus](../podman_app_prometheus), [podman_app_grafana](../podman_app_grafana),
[podman_app_apprise](../podman_app_apprise) and [podman_app_proxy_nginx](../podman_app_proxy_nginx).

## Rootless (default) or rootful

By default apps run rootless, as the account Ansible connects as (or
`podman_app_rootless_user`). Quadlets go in `~/.config/containers/systemd`,
config in `~/<name>`, and services run under the user's systemd. Lingering is
enabled for the account (`podman_app_linger`), so its services run without a
login session and start at boot; that step needs sudo the first time. Rootless
apps cannot publish ports below 1024.

Set `podman_app_rootless: false` to run rootful, as root, with quadlets in
`/etc/containers/systemd` and config in `/etc/<name>`.

The role uses `become` to switch to the account that runs the app, so works
whether Ansible connects as that account or as another user with sudo.

### Config files

Each `podman_app_config_files` item is `{src, dest, mode, template}`. `dest`
is a path inside the config directory, and parent directories are created.
`mode` defaults to `0644` (many images run as a non-root user that must read
the file), so set `0600` for secrets. `template` defaults to true; set it
false to copy the file as is, eg when it contains Go template syntax like
`{{ $labels }}`. A directory `src` ending in `/`, with `template: false`, is
copied recursively.

To mount a single file rather than the whole config directory, leave
`podman_app_config_mount` empty and add a volume for it, eg
`%h/starloom/config.yaml:/config/config.yaml:ro,Z`. Use `%h` (the systemd
specifier for the user's home directory) rather than `~`, which quadlets do
not expand.

With `podman_app_reload_signal` (eg `HUP`), a change to config files alone
sends that signal so the app reloads them, rather than restarting it.

Some images take ownership of what is mounted at their config path when they
start (eg `chown -R` in the entrypoint). Run rootless, that leaves the config
directory owned by a container user, so the next run cannot update the files.
For those images, mount single files read-only, pass settings as environment
variables, or use a named volume, rather than `podman_app_config_mount`.

### Secrets

`podman_app_env` is written into the quadlet, which other users can read. Put
passwords in `podman_app_secret_env` instead: it is written to a `0600` env file
in the config directory and passed with `EnvironmentFile=`.

### Multi-container stacks

Deploy each container as its own app, and join them with:

- `podman_app_networks`: containers on the same network reach each other by
  container name. Each network is created automatically (via a `.network`
  quadlet), unless it is a built-in mode like `host`.
- `podman_app_network_aliases`: extra names to be reached by, eg `mysql`.
- `podman_app_requires`: apps that must start first. If they have a
  `podman_app_healthcheck`, this app waits until they are healthy (the
  equivalent of compose's `depends_on: condition: service_healthy`).
  Restarting a required app also restarts the apps that require it.
- `podman_app_service_extra: TimeoutStartSec=180` limits how long a start (eg
  waiting for a healthy dependency) can take.

`podman_app_exec` sets the container's arguments (replacing the image's
`CMD`), and `podman_app_labels` its labels. Anything else quadlets support can
be added with the `*_extra` variables, eg `podman_app_quadlet_extra: UserNS=keep-id`
or `DNS=192.168.0.1`.

## Removing an app

Set `podman_app_state: absent` to stop the app and remove its quadlet. Its
config files, secret env file, volumes and networks are kept, as they may hold
data or be shared; remove those yourself once you are sure.

## Image updates

With `podman_app_tag_update` (the default), every run pulls `podman_app_image`
again. If that gets a new image, eg a newer `:latest`, the service is restarted,
which recreates the container from the new image. If the image is unchanged,
nothing restarts. If the pull fails but an image is already present, the app
keeps running it. Set it to false to only pull an image when it is missing.

To have Renovate propose updates to pinned tags instead, see
[Renovate](../../README.md#renovate).

## Publishing an app at an address

Set `podman_app_external_address` (eg `prometheus.example.com`) and the app is
added to the `podman_app_external_apps` host fact. Run one of the proxy roles
later in the same play and it creates a reverse proxy vhost for each of them:

- [podman_app_proxy_nginx](../podman_app_proxy_nginx) (nginx, in a container)
- [systemd_service_proxy_httpd](../systemd_service_proxy_httpd) (host httpd)
- [systemd_service_proxy_haproxy](../systemd_service_proxy_haproxy) (host haproxy)

This role never writes proxy config itself, so it does not depend on any of
them. `podman_app_external_title`, `_description` and `_category` are carried
in the same fact, for catalogues of apps such as a homepage.

The upstream is worked out from the first of `podman_app_ports`: `9090:9090`
proxies to `http://127.0.0.1:9090/`, and `10.0.0.5:8081:8080` to
`http://10.0.0.5:8081/`. Set `podman_app_external_upstream` to override it,
eg for apps using `podman_app_networks: [host]`.

Every app (published or not) is also added to the `podman_app_apps` host fact,
which [systemd_service_olivetin](../systemd_service_olivetin) uses to make
start, stop, restart and update actions for each app.

Both facts are recorded whatever `--tags` a run uses, so a run limited to the
proxy's tags still sees every app.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `podman_app_name` | (required) | Container and systemd service name. |
| `podman_app_image` | (required) | Fully qualified image, eg docker.io/prom/prometheus:latest. |
| `podman_app_state` | `present` | present deploys the app. absent stops it and removes its quadlet, keeping its config files, volumes and networks. |
| `podman_app_rootless` | `True` | Run as a rootless user. False runs rootful, as root. |
| `podman_app_rootless_user` |  | Account to run a rootless app as. Empty uses the account Ansible connects as. |
| `podman_app_linger` | `True` | Enable lingering for the rootless user, so its services run without a login session and start at boot. Needs sudo (become) the first time. |
| `podman_app_ports` | `[]` | Published ports, eg "9090:9090" or "127.0.0.1:8081:8080". Rootless apps cannot publish ports below 1024. |
| `podman_app_volumes` | `[]` | Volumes, as named-volume:path or /host/path:path[:options]. |
| `podman_app_env` | `{}` | Environment variables for the container. Written into the quadlet, so not for secrets. |
| `podman_app_secret_env` | `{}` | Secret environment variables, written to a 0600 env file in the config directory instead of the quadlet. |
| `podman_app_container_user` |  | User to run as inside the container, eg 1000:1000. Empty uses the image default. |
| `podman_app_exec` |  | Arguments for the container, replacing the image's default command (CMD), eg --config.file=/etc/app.yml. |
| `podman_app_labels` | `{}` | Container labels. |
| `podman_app_networks` | `[]` | Podman networks to join. Containers on a network reach each other by container name. Each is created via a .network quadlet, unless it is a built-in mode (host, none, private, bridge, pasta, slirp4netns). |
| `podman_app_network_aliases` | `[]` | Extra names other containers can reach this one by, eg mysql. |
| `podman_app_requires` | `[]` | Other apps this app needs, by podman_app_name (or full systemd unit names). They start first, and if they have a healthcheck, this app waits until they are healthy. |
| `podman_app_healthcheck` | `{}` | Healthcheck. Apps that require this one wait until it is healthy. Empty for no healthcheck. |
| `podman_app_config_dir` |  | Host directory for config files. Empty uses ~/<name> when rootless, or /etc/<name> when rootful. |
| `podman_app_config_mount` |  | Path in the container to mount the config directory at. Empty does not mount it. |
| `podman_app_config_files` | `[]` | Files (or directories) to write into the config directory. |
| `podman_app_reload_signal` |  | Signal (eg HUP) that makes the app reload its config files. When set, a change to config files alone sends this signal instead of restarting the app. |
| `podman_app_unit_extra` |  | Raw lines appended to the [Unit] section of the quadlet. |
| `podman_app_quadlet_extra` |  | Raw lines appended to the [Container] section of the quadlet, eg UserNS=keep-id. |
| `podman_app_service_extra` |  | Raw lines appended to the [Service] section of the quadlet, eg TimeoutStartSec=180. |
| `podman_app_tag_update` | `True` | Pull podman_app_image on every run, especially useful for tags like :latest. If the pull gets a new image, the service is restarted, which recreates the container from it. |
| `podman_app_external_address` |  | Hostname to publish this app at, eg prometheus.example.com. When set, the app is added to the podman_app_external_apps host fact, which the proxy roles turn into reverse proxy vhosts. |
| `podman_app_external_upstream` |  | Upstream URL for the proxy, eg http://127.0.0.1:9090/. Empty derives it from the first of podman_app_ports. |
| `podman_app_external_title` |  | Title for catalogues of apps (eg a homepage), recorded in podman_app_external_apps. Empty uses podman_app_name. |
| `podman_app_external_description` |  | One-line description for catalogues of apps. |
| `podman_app_external_category` |  | Category for catalogues of apps. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

The role can be used several times in one play, once per app. To select apps
with `--tags`, list them under `roles:`, or give `include_role` an
`apply: {tags: [...]}`; tags on an `include_role` task alone are not passed to
the tasks inside it.

An app with a database, published behind the proxy:

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app
      tags: [apps]
      vars:
        podman_app_name: mariadb
        podman_app_image: docker.io/mariadb:11.8
        podman_app_networks: [apps]
        podman_app_network_aliases: [mysql]
        podman_app_volumes:
          - mariadb-data:/var/lib/mysql
        podman_app_env:
          MARIADB_DATABASE: japella
          MARIADB_USER: japella
        podman_app_secret_env:
          MARIADB_ROOT_PASSWORD: "{{ vault_japella_db_root_password }}"
          MARIADB_PASSWORD: "{{ vault_japella_db_password }}"
        podman_app_healthcheck:
          cmd: healthcheck.sh --connect --innodb_initialized
          interval: 10s
          retries: 10
          start_period: 30s

    - role: jamesread.soe.podman_app
      tags: [apps]
      vars:
        podman_app_name: japella
        podman_app_image: ghcr.io/jamesread/japella:latest
        podman_app_networks: [apps]
        podman_app_requires: [mariadb]
        podman_app_ports:
          - 127.0.0.1:8089:8080
        podman_app_secret_env:
          JAPELLA_DB_PASS: "{{ vault_japella_db_password }}"
        podman_app_service_extra: TimeoutStartSec=180
        podman_app_external_address: japella.example.com
        podman_app_external_description: Social media and chat powertool

    - role: jamesread.soe.podman_app_proxy_nginx
      tags: [proxy]
```

The Prometheus Google Calendar and Gmail exporters (these replace the old
`podman_prom_gcal_exporter` and `podman_prom_gmail_exporter` roles).
`gcal-secrets.json`, `gcal.cfg`, etc are templates in your playbook's
`templates/` directory.

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app
      vars:
        podman_app_name: prom-gcal-exporter
        podman_app_image: docker.io/jamesread/prometheus-google-calendar-exporter:latest
        podman_app_ports:
          - 8081:8080
        podman_app_config_mount: /root/.prometheus-gcal-exporter
        podman_app_config_files:
          - src: gcal-secrets.json
            dest: client_secret.json
            mode: '0600'
          - src: gcal.cfg
            dest: prometheus-gcal-exporter.cfg

    - role: jamesread.soe.podman_app
      vars:
        podman_app_name: prometheus-gmail-exporter
        podman_app_image: docker.io/jamesread/prometheus-gmail-exporter:latest
        podman_app_ports:
          - 8082:8080
        podman_app_config_mount: /root/.prometheus-gmail-exporter
        podman_app_config_files:
          - src: gmail-secrets.json
            dest: client_secret.json
            mode: '0600'
          - src: gmail.cfg
            dest: prometheus-gmail-exporter.cfg
```
