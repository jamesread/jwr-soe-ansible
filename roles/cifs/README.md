# cifs

Mount a CIFS share.
## Variables
| Variable | Default |
|----------|---------|
| `cifs_username` | unset |
| `cifs_password` | unset |


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.cifs
      vars:
        cifs_username: unset
        cifs_password: unset
```
