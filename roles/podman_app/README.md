# podman_app

Runs any container image as a systemd service, using a [Podman quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html).

Writes `/etc/containers/systemd/<podman_app_name>.container`, plus any config
files into `podman_app_config_dir`, and restarts the service only when one of
those changes. The service starts at boot. Requires rootful podman 4.4 or newer.

Common apps have their own wrapper roles with sensible defaults, eg
[podman_app_prometheus](../podman_app_prometheus) and [podman_app_grafana](../podman_app_grafana).
## Variables
| Variable | Default |
|----------|---------|
| `podman_app_name` | (required) |
| `podman_app_image` | (required) |
| `podman_app_ports` | [] |
| `podman_app_volumes` | [] |
| `podman_app_env` | {} |
| `podman_app_user` |  |
| `podman_app_config_dir` | /etc/{{ podman_app_name }} |
| `podman_app_config_mount` |  |
| `podman_app_config_files` | [] |
| `podman_app_quadlet_extra` |  |

Each `podman_app_config_files` item is `{src, dest, mode, template}`. `mode`
defaults to `0644` (many images run as a non-root user that must read the file),
so set `0600` for secrets. `template` defaults to true; set it false to copy the
file as is, eg when it contains Go template syntax like `{{ $labels }}`.

## Example usage in a playbook

The role can be used several times in one play, once per app. These two
replace the old `podman_prom_gcal_exporter` and `podman_prom_gmail_exporter`
roles. `gcal-secrets.json`, `gcal.cfg`, etc are templates in your playbook's
`templates/` directory.

```yaml
- hosts: [myserver]
  tasks:
    - name: Google Calendar Prometheus exporter
      ansible.builtin.include_role:
        name: jamesread.soe.podman_app
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

    - name: Gmail Prometheus exporter
      ansible.builtin.include_role:
        name: jamesread.soe.podman_app
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
