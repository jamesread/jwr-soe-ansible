# podman_dashboard

Installs a Dashboard container.
## Variables
| Variable | Default |
|----------|---------|
| `dashboard_volume` | /containers/dashboard/ |
| `dashboard_config` | dashboard.json |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_dashboard
      vars:
        dashboard_volume: /containers/dashboard/
        dashboard_config: dashboard.json
```
