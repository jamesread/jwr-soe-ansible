# systemd_service_haproxy

Installs haproxy as a service.
## Variables
* `cfg_file` (default: haproxy.cfg)


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.systemd_service_haproxy
      vars:
        cfg_file: haproxy.cfg
```
