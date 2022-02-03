# podman_grafana

Installs a Grafana container.
## Variables
| Variable | Default |
|----------|---------|
| `cfg_grafana_installed` | True |
| `container_podman_volume` | /containers/grafana/ |


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_grafana
      vars:
        cfg_grafana_installed: True
        container_podman_volume: /containers/grafana/
```
