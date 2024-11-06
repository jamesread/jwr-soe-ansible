# podman_prom_gcal_exporter

Installs a Google Calendar Prometheus exporter.
## Variables
| Variable | Default |
|----------|---------|
| `config_file` | gcal.cfg |
| `secret_file` | secrets.json |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_prom_gcal_exporter
      vars:
        config_file: gcal.cfg
        secret_file: secrets.json
```
