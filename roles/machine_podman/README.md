# machine_podman

Installs podman.
## Variables
| Variable | Default |
|----------|---------|
| `machine_podman_traefik_installed` | False |
| `machine_podman_haproxy_cfg` | haproxy.cfg.j2 |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.machine_podman
      vars:
        machine_podman_traefik_installed: False
        machine_podman_haproxy_cfg: haproxy.cfg.j2
```
