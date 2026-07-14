# podman_prom_gmail_exporter

Installs a gmail exporter container.
## Variables
| Variable | Default |
|----------|---------|
| `podman_prom_gmail_exporter_config_file` | gmail.cfg |
| `podman_prom_gmail_exporter_secret_file` | secrets.json |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_prom_gmail_exporter
      vars:
        podman_prom_gmail_exporter_config_file: gmail.cfg
        podman_prom_gmail_exporter_secret_file: secrets.json
```
