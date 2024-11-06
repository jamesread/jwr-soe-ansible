# machine_podman

Installs podman.
## Variables
| Variable | Default |
|----------|---------|
| `cfg_traefik_installed` | False |
| `cfg_haproxy` | haproxy.cfg.j2 |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles
    - roles: jamesread.soe.machine_podman
      vars:
        cfg_traefik_installed: False
        cfg_haproxy: haproxy.cfg.j2
```
