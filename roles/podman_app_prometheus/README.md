# podman_app_prometheus

Runs Prometheus as a systemd service (podman quadlet), using [podman_app](../podman_app).
Rootless by default, like `podman_app`.

Config goes in the config directory (`~/prometheus` rootless, `/etc/prometheus`
rootful), mounted at `/etc/prometheus`. Data is in the `prometheus-data`
named volume, and the web UI is on port 9090. A change to the config or alert
rules is applied with SIGHUP, without restarting Prometheus.

The alert rules file is copied as is, not templated, because rules use Go
template syntax such as `{{ $labels }}`.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `podman_app_prometheus_image` | `docker.io/prom/prometheus:latest` | Prometheus container image. |
| `podman_app_prometheus_ports` | `['9090:9090']` | Published ports, as for podman_app_ports. |
| `podman_app_prometheus_cfg_file` | `prometheus.yml` | Prometheus config template, written to prometheus.yml in the config directory. |
| `podman_app_prometheus_alert_file` | `alert.rules` | Alert rules file, copied as is (not templated) to alert.rules in the config directory. |
| `podman_app_prometheus_extra_args` | `[]` | Extra command line arguments, eg --web.external-url=https://prom.example.com/. |
| `podman_app_prometheus_external_address` |  | Hostname to publish Prometheus at, via a proxy role (see podman_app_external_address). Empty does not publish it. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app_prometheus
      vars:
        podman_app_prometheus_cfg_file: prometheus.yml
        podman_app_prometheus_alert_file: alert.rules
        podman_app_prometheus_extra_args:
          - --web.external-url=https://prom.example.com/
        podman_app_prometheus_external_address: prom.example.com
```
