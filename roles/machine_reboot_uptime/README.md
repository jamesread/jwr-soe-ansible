# machine_reboot_uptime

Reboots the host when its uptime is over `machine_reboot_uptime_days`, with
Apprise notifications, and waits for it to come back. **Applying this role is
an action**: run it from a schedule (eg weekly), so hosts pick up new kernels
and libraries without anyone remembering to reboot them.

Hosts with less uptime are left alone. A failed reboot is notified, and
reboots are logged to `machine_reboot_uptime_log_file`.

See [Apprise notifications](../../README.md#apprise-notifications) for where
notifications are sent. Run with `--tags notify` to send a test notification
without rebooting.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `machine_reboot_uptime_days` | `5` | Reboot when uptime is more than this many days. 5 keeps uptime under about a week when run weekly. |
| `machine_reboot_uptime_timeout` | `600` | Seconds to wait for the host to come back. |
| `machine_reboot_uptime_log_file` | `/var/log/soe-reboot-uptime.log` | Log of reboots on the host. |
| `machine_reboot_uptime_apprise_host` | `{{ apprise_host \| default('') }}` | Apprise API to send to, eg http://apprise.example.com:8000. Defaults to the host's apprise_host. Empty runs Apprise on this host (podman_app_apprise), listening on 127.0.0.1 only. |
| `machine_reboot_uptime_apprise_key` | `{{ apprise_key \| default('') }}` | Config key on the Apprise API to send to (/notify/<key>). Defaults to the host's apprise_key. Empty sends to /notify, which the local Apprise sends to podman_app_apprise_urls. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [all]
  serial: 1
  roles:
    - role: jamesread.soe.machine_reboot_uptime
```
