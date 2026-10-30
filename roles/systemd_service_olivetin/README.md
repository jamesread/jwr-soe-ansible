# systemd_service_olivetin

Installs [OliveTin](https://www.olivetin.app/) (safe web buttons for shell
commands) as a service on the host, from its GitHub release rpm, pinned to
`systemd_service_olivetin_version`. Renovate can bump the version (see the
collection README).

Your config lives in the environment repo, eg `files/OliveTin/`, and is copied
to `/etc/OliveTin` (`systemd_service_olivetin_config_src`): `config.yaml`, plus
any `config.d/` fragments, `entities/`, `custom-webui/` and so on. File modes
are kept, so give secrets (eg an SSH key for actions) `0600` in the repo.
Fragments removed from the repo are removed from the host. `config.yaml` must
have `include: config.d` for fragments to load.

## Actions for podman apps

By default, every [podman_app](../podman_app) app on the host gets Start,
Stop, Restart and Update (pull the image's tag and restart onto it) actions,
grouped on a "Podman apps" dashboard. They are generated into
`config.d/50-podman-apps.yaml` from the `podman_app_apps` fact, so run this
role after the apps, in the same play. Action ids are stable
(`podman-app-<name>-<verb>`), for use in other config and scripts.

They use systemd, so work with quadlets (stopping the container directly would
just make systemd restart it), for both rootful and rootless apps.

To publish OliveTin itself, add a vhost to your proxy, eg
`{server_name: ot.example.com, upstream: http://127.0.0.1:1337/}`.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `systemd_service_olivetin_version` | `3000.20.0` | OliveTin release to install. Renovate can bump it (see the collection README). |
| `systemd_service_olivetin_rpm_url` | `https://github.com/OliveTin/OliveTin/releases/download/{{ systemd_service_olivetin_version }}/OliveTin_linux_{{ 'arm64' if ansible_facts['architecture'] \| default('x86_64') == 'aarch64' else 'amd64' }}.rpm` | URL of the OliveTin rpm. Defaults to the GitHub release for the version and architecture. |
| `systemd_service_olivetin_config_dir` | `/etc/OliveTin` | OliveTin config directory. |
| `systemd_service_olivetin_config_src` |  | Directory of OliveTin config in your playbook's files, copied to the config directory. config.yaml, and optionally config.d/, entities/, custom-webui/ and so on. Empty keeps the packaged config. |
| `systemd_service_olivetin_config_d_prune` | `True` | Remove fragments in config.d/ that are not in config_src. |
| `systemd_service_olivetin_podman_app_actions` | `True` | Generate start, stop, restart and update actions (and a dashboard) for every podman_app app on this host, in config.d/50-podman-apps.yaml. Run this role after the podman_app roles in the same play, as it reads the podman_app_apps fact they set. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app
      vars:
        podman_app_name: japella
        podman_app_image: ghcr.io/jamesread/japella:latest

    - role: jamesread.soe.systemd_service_olivetin
      vars:
        systemd_service_olivetin_config_src: OliveTin
```
