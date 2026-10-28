# podman_app_prometheus

Runs Prometheus as a systemd service (podman quadlet), using [podman_app](../podman_app).

Config goes in `/etc/prometheus`, data in the `prometheus-data` named volume,
and the web UI is on port 9090. Changing the config restarts Prometheus.
## Variables
| Variable | Default |
|----------|---------|
| `podman_app_prometheus_image` | docker.io/prom/prometheus:latest |
| `podman_app_prometheus_cfg_file` | prometheus.yml |
| `podman_app_prometheus_alert_file` | alert.rules |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app_prometheus
      vars:
        podman_app_prometheus_image: docker.io/prom/prometheus:latest
        podman_app_prometheus_cfg_file: prometheus.yml
        podman_app_prometheus_alert_file: alert.rules
```
