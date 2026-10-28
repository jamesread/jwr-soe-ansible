# podman_app_grafana

Runs Grafana as a systemd service (podman quadlet), using [podman_app](../podman_app).

The web UI is on port 3000.
## Variables
| Variable | Default |
|----------|---------|
| `podman_app_grafana_image` | docker.io/grafana/grafana:latest |
| `podman_app_grafana_volume` | /containers/grafana |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app_grafana
      vars:
        podman_app_grafana_image: docker.io/grafana/grafana:latest
        podman_app_grafana_volume: /containers/grafana
```
