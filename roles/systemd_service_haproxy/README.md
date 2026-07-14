# systemd_service_haproxy

Installs haproxy as a service.
## Variables
| Variable | Default |
|----------|---------|
| `systemd_service_haproxy_cfg_file` | haproxy.cfg |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.systemd_service_haproxy
      vars:
        systemd_service_haproxy_cfg_file: haproxy.cfg
```
