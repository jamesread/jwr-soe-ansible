# machine_upgrade_fedora_release

Upgrades Fedora to the next release (n+1) when one is available, with Apprise
notifications. **Applying this role is an action**: run it from a schedule (eg
an OliveTin cron or a systemd timer on the control host), not from a host's
everyday playbook.

Each run checks whether the next release is available and no higher than
`machine_upgrade_fedora_release_max`. If not, the host is left alone. If so,
it updates the current release, downloads the upgrade, notifies, and reboots
into the offline upgrade (which reboots again when done). Failures are
notified, and every step is logged to `machine_upgrade_fedora_release_log_file`.
Hosts other than Fedora are skipped.

See [Apprise notifications](../../README.md#apprise-notifications) for where
notifications are sent. Run with `--tags notify` to send a test notification
without upgrading.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `machine_upgrade_fedora_release_max` | `44` | Highest release to upgrade to. Stops upgrades onto a release before it is final; bump it when a new Fedora release ships. |
| `machine_upgrade_fedora_release_log_file` | `/var/log/soe-upgrade-fedora-release.log` | Log of upgrade steps on the host. |
| `machine_upgrade_fedora_release_apprise_host` | `{{ apprise_host \| default('') }}` | Apprise API to send to, eg http://apprise.example.com:8000. Defaults to the host's apprise_host. Empty runs Apprise on this host (podman_app_apprise), listening on 127.0.0.1 only. |
| `machine_upgrade_fedora_release_apprise_key` | `{{ apprise_key \| default('') }}` | Config key on the Apprise API to send to (/notify/<key>). Defaults to the host's apprise_key. Empty sends to /notify, which the local Apprise sends to podman_app_apprise_urls. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [all]
  roles:
    - role: jamesread.soe.machine_upgrade_fedora_release
      vars:
        machine_upgrade_fedora_release_max: 44
```
