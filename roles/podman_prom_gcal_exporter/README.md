# podman_prom_gcal_exporter

Installs a Google Calendar Prometheus exporter.
## Variables
| Variable | Default |
|----------|---------|
| `podman_prom_gcal_exporter_config_file` | gcal.cfg |
| `podman_prom_gcal_exporter_secret_file` | secrets.json |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_prom_gcal_exporter
      vars:
        podman_prom_gcal_exporter_config_file: gcal.cfg
        podman_prom_gcal_exporter_secret_file: secrets.json
```
