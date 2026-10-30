# machine_notify_boot

Sends an Apprise notification each time the host boots, eg
`myhost has booted up, os Fedora Linux 44 (Server Edition)`, from a systemd
oneshot service (`soe-notify-boot`). A failed notification never delays or
fails the boot.

See [Apprise notifications](../../README.md#apprise-notifications) for where
notifications are sent. Run with `--tags notify` to send a test notification.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `machine_notify_boot_apprise_host` | `{{ apprise_host \| default('') }}` | Apprise API to send to, eg http://apprise.example.com:8000. Defaults to the host's apprise_host. Empty runs Apprise on this host (podman_app_apprise), listening on 127.0.0.1 only. |
| `machine_notify_boot_apprise_key` | `{{ apprise_key \| default('') }}` | Config key on the Apprise API to send to (/notify/<key>). Defaults to the host's apprise_key. Empty sends to /notify, which the local Apprise sends to podman_app_apprise_urls. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [all]
  roles:
    - role: jamesread.soe.machine_notify_boot
```
