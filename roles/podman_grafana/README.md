# podman_grafana

Installs a Grafana container.
## Variables
| Variable | Default |
|----------|---------|
| `podman_grafana_installed` | True |
| `podman_grafana_volume` | /containers/grafana |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_grafana
      vars:
        podman_grafana_installed: True
        podman_grafana_volume: /containers/grafana
```
