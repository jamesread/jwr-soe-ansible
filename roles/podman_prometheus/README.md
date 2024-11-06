# podman_prometheus

Installs a Prometheus container.
## Variables
| Variable | Default |
|----------|---------|
| `cfg_file` | prometheus.yml |
| `alert_file` | alert.rules |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_prometheus
      vars:
        cfg_file: prometheus.yml
        alert_file: alert.rules
```
