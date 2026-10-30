# podman_app_grafana

Runs Grafana as a systemd service (podman quadlet), using [podman_app](../podman_app).
Rootless by default, like `podman_app`.

Data is in the `grafana-data` named volume, and the web UI is on port 3000. To
keep existing data in a host directory instead, override
`podman_app_grafana_volumes`, eg `['/containers/grafana_data:/var/lib/grafana:Z']`
(Grafana runs as uid 472 in the container).

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `podman_app_grafana_image` | `docker.io/grafana/grafana:latest` | Grafana container image. |
| `podman_app_grafana_ports` | `['3000:3000']` | Published ports, as for podman_app_ports. |
| `podman_app_grafana_volumes` | `['grafana-data:/var/lib/grafana']` | Volumes, as for podman_app_volumes. Override to keep existing data in a host directory. |
| `podman_app_grafana_env` | `{}` | Grafana settings as environment variables, eg GF_SERVER_ROOT_URL. |
| `podman_app_grafana_external_address` |  | Hostname to publish Grafana at, via a proxy role (see podman_app_external_address). Empty does not publish it. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app_grafana
      vars:
        podman_app_grafana_env:
          GF_SERVER_ROOT_URL: https://grafana.example.com/
        podman_app_grafana_external_address: grafana.example.com
```
