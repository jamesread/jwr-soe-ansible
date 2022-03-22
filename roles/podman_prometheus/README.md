# podman_prometheus

Installs a Prometheus container.
## Variables
| Variable | Default |
|----------|---------|
| `cfg_file` | prometheus.yml |


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_prometheus
      vars:
        cfg_file: prometheus.yml
```
