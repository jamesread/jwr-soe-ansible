# machine_hardening_auth

Hardens SSH authentication and adds a fail2ban sshd jail. The hardening
settings take priority over every other sshd setting on the host.

sshd uses the first value it reads for each option, so the role:

- Installs a drop-in, `/etc/ssh/sshd_config.d/00-<label>-hardening.conf`,
  named to sort before the other drop-ins (eg cloud-init's `50-cloud-init.conf`).
- Puts the same settings in a marked block at the very top of
  `/etc/ssh/sshd_config`, before its `Include` of the drop-ins, so they also
  win over settings in `sshd_config` itself. A block left further down the
  file, eg by an older version of this role, is moved to the top.
- Checks `sshd -T` afterwards and fails the run if any setting, or
  `AllowUsers`, did not take effect (`machine_hardening_auth_verify`), eg
  because a `Match` block overrides it.

Both files are validated with `sshd -t` before being written.

`machine_hardening_auth_ssh_allow_users` becomes `AllowUsers`. **Include the
Ansible login user**, or the next run will lock you out. Give times in
`machine_hardening_auth_sshd_options` in seconds, as `sshd -T` reports them.

Also installs fail2ban with an sshd jail (systemd backend). Database hardening
is deliberately out of scope.

Note: `jamesread.soe.common` also edits `sshd_config` (`UseDNS no`). The two
roles do not conflict.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `machine_hardening_auth_label` | `soe` | Label used in the drop-in filename, blockinfile marker and file headers. |
| `machine_hardening_auth_header` | `Managed by Ansible — {{ machine_hardening_auth_label }} auth hardening` | Comment header written at the top of managed files. |
| `machine_hardening_auth_sshd_dropin` | `/etc/ssh/sshd_config.d/00-{{ machine_hardening_auth_label }}-hardening.conf` | Path of the sshd_config.d drop-in. |
| `machine_hardening_auth_sshd_config_block` | `True` | Also put the settings at the top of /etc/ssh/sshd_config, before its Include line, so they win over everything else. |
| `machine_hardening_auth_sshd_options` | `{ClientAliveCountMax: 2, ClientAliveInterval: 300, KbdInteractiveAuthentication: 'no', LogLevel: VERBOSE, LoginGraceTime: 30, MaxAuthTries: 3, PasswordAuthentication: 'no', PermitEmptyPasswords: 'no', PermitRootLogin: 'no', PubkeyAuthentication: 'yes', X11Forwarding: 'no'}` | Ordered sshd options written to the drop-in and config block. Give times in seconds, as they are verified against sshd -T. |
| `machine_hardening_auth_ssh_allow_users` | `[]` | AllowUsers entries. Empty omits AllowUsers. Include ansible_user. |
| `machine_hardening_auth_verify` | `True` | Fail the run if sshd -T shows any hardening option or AllowUsers did not take effect. |
| `machine_hardening_auth_fail2ban` | `True` | Install and configure the fail2ban sshd jail. |
| `machine_hardening_auth_fail2ban_findtime` | `10m` | fail2ban findtime. |
| `machine_hardening_auth_fail2ban_bantime` | `1h` | fail2ban bantime. |
| `machine_hardening_auth_fail2ban_maxretry` | `5` | fail2ban maxretry. |

<!-- END GENERATED VARIABLES -->

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
