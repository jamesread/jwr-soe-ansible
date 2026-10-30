# podman_efk

Installs a EFK stack.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `podman_efk_elastic_password` |  | Elasticsearch elastic user password (required; set via Vault). |
| `podman_efk_kibana_encryption_key` |  | Kibana xpack.security.encryptionKey (required; set via Vault). |
| `podman_efk_elasticsearch_host` | `http://10.88.0.1:9200` | Elasticsearch URL for Kibana. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_efk
```
