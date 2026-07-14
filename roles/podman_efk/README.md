# podman_efk

Installs a EFK stack.
## Variables
| Variable | Default |
|----------|---------|
| `podman_efk_elastic_password` |  |
| `podman_efk_kibana_encryption_key` |  |
| `podman_efk_elasticsearch_host` | http://10.88.0.1:9200 |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_efk
      vars:
        podman_efk_elastic_password:
        podman_efk_kibana_encryption_key:
        podman_efk_elasticsearch_host: http://10.88.0.1:9200
```
