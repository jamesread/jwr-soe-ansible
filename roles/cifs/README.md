# cifs

Mount a CIFS share.
## Variables
* `cifs_username` (default: unset)
* `cifs_password` (default: unset)


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.cifs
      vars:
        cifs_username: unset
        cifs_password: unset
```
