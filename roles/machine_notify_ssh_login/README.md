# machine_notify_ssh_login

Sends an Apprise notification when someone opens an interactive SSH login, eg
`alice logged in to myhost from 192.0.2.10`.

It is a `/etc/profile.d` script, so it fires once per login shell with a
terminal: not for `scp`, `sftp`, one-off `ssh host command` runs or Ansible.
It sends in the background, so a slow or missing Apprise never delays the login.

The script runs as the logged-in user and posts straight to the Apprise API,
so (unlike a root-only sender) it needs no sudo rule. Any local user can
therefore also send notifications through the local Apprise.

See [Apprise notifications](../../README.md#apprise-notifications) for where
notifications are sent. Run with `--tags notify` to send a test notification.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `machine_notify_ssh_login_apprise_host` | `{{ apprise_host \| default('') }}` | Apprise API to send to, eg http://apprise.example.com:8000. Defaults to the host's apprise_host. Empty runs Apprise on this host (podman_app_apprise), listening on 127.0.0.1 only. |
| `machine_notify_ssh_login_apprise_key` | `{{ apprise_key \| default('') }}` | Config key on the Apprise API to send to (/notify/<key>). Defaults to the host's apprise_key. Empty sends to /notify, which the local Apprise sends to podman_app_apprise_urls. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [all]
  roles:
    - role: jamesread.soe.machine_notify_ssh_login
```
