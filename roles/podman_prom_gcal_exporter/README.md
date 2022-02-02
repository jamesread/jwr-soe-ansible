# podman_prom_gcal_exporter

Installs a Google Calendar Prometheus exporter.
## Variables
* `config_file` (default: gcal.cfg)
* `secret_file` (default: secrets.json)


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.podman_prom_gcal_exporter
      vars:
        config_file: gcal.cfg
        secret_file: secrets.json
```
