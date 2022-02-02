# podman_dashboard

Installs a Grafana container.
## Variables
* `dashboard_volume` (default: /containers/dashboard/)
* `dashboard_config` (default: dashboard.json)


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_dashboard
      vars:
        dashboard_volume: /containers/dashboard/
        dashboard_config: dashboard.json
```
