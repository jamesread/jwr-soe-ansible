# containerhost_podman

Installs podman.
## Variables
* `cfg_traefik_installed` (default: False)
* `cfg_haproxy` (default: haproxy.cfg.j2)


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.containerhost_podman
      vars:
        cfg_traefik_installed: False
        cfg_haproxy: haproxy.cfg.j2
```
