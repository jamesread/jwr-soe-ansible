# machine_podman

Installs podman.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `machine_podman_haproxy_cfg` | `haproxy.cfg.j2` | HAProxy config template name when used with related roles. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.machine_podman
```
