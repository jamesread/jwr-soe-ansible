# podman_app_apprise

Runs the [Apprise API](https://github.com/caronc/apprise-api), using
[podman_app](../podman_app), so programs on this host can send notifications
(Telegram, email, ntfy, and many more) with a plain HTTP request.

It is published on `127.0.0.1` only, never on an external interface. It runs
rootful by default, so it starts at boot for machine-level notifications.

Notifications go to the [Apprise URLs](https://github.com/caronc/apprise/wiki)
in `podman_app_apprise_urls`. They hold tokens, so keep them in a vault; they
are passed to the container in a `0600` env file, not in its unit file. Then
send with:

```bash
curl -X POST --data-urlencode "title=Hello" --data-urlencode "body=World" \
  http://127.0.0.1:8000/notify
```

The `machine_notify_*`, [machine_upgrade_fedora_release](../machine_upgrade_fedora_release)
and [machine_reboot_uptime](../machine_reboot_uptime) roles deploy this role
for themselves, unless the host sets `apprise_host`.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `podman_app_apprise_image` | `docker.io/caronc/apprise:latest` | Apprise API container image. |
| `podman_app_apprise_port` | `8000` | Port on 127.0.0.1 to publish the API on. It is never published on other interfaces. |
| `podman_app_apprise_urls` | `[]` | Apprise URLs that notifications sent to /notify go to, eg tgram://bottoken/ChatID. They hold tokens, so keep them in a vault. |
| `podman_app_apprise_rootless` | `False` | Run rootless. Rootful by default, so it runs from boot for machine-level notifications. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app_apprise
      vars:
        podman_app_apprise_urls:
          - "{{ vault_telegram_apprise_url }}"
```
