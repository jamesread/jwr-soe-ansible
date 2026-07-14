# podman_dashboard

Installs a Dashboard container.
## Variables
| Variable | Default |
|----------|---------|
| `podman_dashboard_volume` | /containers/dashboard/ |
| `podman_dashboard_config` | dashboard.json |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_dashboard
      vars:
        podman_dashboard_volume: /containers/dashboard/
        podman_dashboard_config: dashboard.json
```
