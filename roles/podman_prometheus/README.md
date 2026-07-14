# podman_prometheus

Installs a Prometheus container.
## Variables
| Variable | Default |
|----------|---------|
| `podman_prometheus_cfg_file` | prometheus.yml |
| `podman_prometheus_alert_file` | alert.rules |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_prometheus
      vars:
        podman_prometheus_cfg_file: prometheus.yml
        podman_prometheus_alert_file: alert.rules
```
