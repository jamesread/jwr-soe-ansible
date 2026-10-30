# systemd_service_certbot

Gets and renews a Let's Encrypt certificate with certbot, using the http-01
challenge.

certbot answers the challenge itself, listening on `127.0.0.1` (port
`systemd_service_certbot_http_port`, 9080) only while it runs, so it never
takes port 80 from the proxy. The proxy on port 80 must forward
`/.well-known/acme-challenge/` to it. The proxy roles do this, and run this
role for you when their `*_certbot` option is set, so you rarely need to use
it directly.

Renewal is by the packaged `certbot-renew.timer`. `systemd_service_certbot_deploy_hook`
runs after the certificate is issued or renewed (eg to reload the proxy), with
`RENEWED_LINEAGE` set to the certificate's live directory. The role sets the
`systemd_service_certbot_live_dir` fact to that directory.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `systemd_service_certbot_domains` | (required) | Domains for the certificate. |
| `systemd_service_certbot_cert_name` | `{{ systemd_service_certbot_domains \| first \| default('') }}` | Name of the certificate, ie its directory under /etc/letsencrypt/live. Defaults to the first domain. |
| `systemd_service_certbot_email` |  | Contact for expiry warnings. Empty registers without an email address. |
| `systemd_service_certbot_http_port` | `9080` | Port on 127.0.0.1 that certbot answers the http-01 challenge on. The proxy on port 80 must forward /.well-known/acme-challenge/ to it. |
| `systemd_service_certbot_deploy_hook` |  | Shell commands run after the certificate is issued or renewed, with RENEWED_LINEAGE set to its live directory, eg to reload the proxy. |
| `systemd_service_certbot_staging` | `False` | Use the Let's Encrypt staging server, for testing. Its certificates are not trusted. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.systemd_service_certbot
      vars:
        systemd_service_certbot_domains:
          - example.com
          - www.example.com
        systemd_service_certbot_email: admin@example.com
        systemd_service_certbot_deploy_hook: systemctl reload httpd
```
