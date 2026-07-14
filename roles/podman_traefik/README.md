# podman_traefik

Installs a traefik container.
## Variables
| Variable | Default |
|----------|---------|
| `podman_traefik_volume` | /containers/traefik/ |
| `podman_traefik_config` | traefik.json |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_traefik
      vars:
        podman_traefik_volume: /containers/traefik/
        podman_traefik_config: traefik.json
```
