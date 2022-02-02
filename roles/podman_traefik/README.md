# podman_traefik

Installs a traefik container.
## Variables
* `traefik_volume` (default: /containers/traefik/)
* `traefik_config` (default: traefik.json)


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_traefik
      vars:
        traefik_volume: /containers/traefik/
        traefik_config: traefik.json
```
