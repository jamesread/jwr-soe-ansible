# machine_hardening_auth

Hardens SSH authentication and adds a fail2ban sshd jail.

- Installs an sshd drop-in (`machine_hardening_auth_sshd_dropin`) and, by default, the same settings as a marked block at the tail of `/etc/ssh/sshd_config`. Both are validated with `sshd -t` before being written.
- `machine_hardening_auth_ssh_allow_users` becomes `AllowUsers`. **Include the Ansible login user**, or the next run will lock you out.
- Installs fail2ban with an aggressive sshd jail (systemd backend).

Database hardening is deliberately out of scope.

Note: `jamesread.soe.common` also edits `sshd_config` (`UseDNS no`). The two roles do not conflict.

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.machine_hardening_auth
      vars:
        machine_hardening_auth_label: myserver
        machine_hardening_auth_ssh_allow_users:
          - app
```
