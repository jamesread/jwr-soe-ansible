# systemd_service_proxy_httpd

Installs httpd (on the host) as a name-based reverse proxy for local
services. An approved alternative to [podman_app_proxy_nginx](../podman_app_proxy_nginx),
with the same vhost options.

- Each entry in `systemd_service_proxy_httpd_vhosts` becomes
  `<conf_dir>/<server_name>.conf`, proxying `/` (including websockets) to
  `upstream`.
- Every [podman_app](../podman_app) app on the host with a
  `podman_app_external_address` also gets a vhost
  (`systemd_service_proxy_httpd_podman_apps`). Run this role after them, in
  the same play.
- Vhosts this role wrote that are no longer wanted (eg an app that was removed)
  are deleted. Other files in the directory are left alone.
- Bespoke vhosts and landing pages go in `systemd_service_proxy_httpd_extra_templates`.
  Their `src` resolves via the playbook search path, so the templates stay in
  the environment repo.
- Config changes trigger a graceful reload.

## HTTPS

Plain HTTP on port 80 by default (eg behind Cloudflare). For HTTPS, either:

- set `systemd_service_proxy_httpd_tls_cert` and `_tls_key` to a certificate
  already on the host (eg a wildcard certificate), or
- set `systemd_service_proxy_httpd_certbot: true` to get a Let's Encrypt
  certificate covering every vhost, with [systemd_service_certbot](../systemd_service_certbot).
  On the first run vhosts start as HTTP only, so the challenge can be answered,
  and switch to HTTPS once the certificate exists. Renewals reload httpd.

With HTTPS, vhosts listen on 443 and port 80 redirects to it. Set `tls: false`
on a vhost to keep it HTTP only.

Unlike `systemd_service_apachephp`, this role installs no PHP and does not
touch firewalld.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `systemd_service_proxy_httpd_manage_packages` | `True` | Install the httpd package (and mod_ssl, when HTTPS is used). |
| `systemd_service_proxy_httpd_conf_dir` | `/etc/httpd/conf.d` | Directory for vhost config files. |
| `systemd_service_proxy_httpd_log_dir` | `/var/log/httpd` | Directory for per-vhost logs. |
| `systemd_service_proxy_httpd_vhosts` | `[]` | Reverse proxy vhosts. Keys are server_name and upstream, plus optional conf_name, tls (default true) and extra (raw lines for the vhost). |
| `systemd_service_proxy_httpd_extra_templates` | `[]` | Extra templates to install. Keys are src and dest, plus optional owner, group and mode. |
| `systemd_service_proxy_httpd_podman_apps` | `True` | Also add a vhost for each podman_app app on this host that sets podman_app_external_address. Run this role after the podman_app roles in the same play, as it reads the podman_app_external_apps fact they set. |
| `systemd_service_proxy_httpd_tls_cert` |  | Certificate (chain) file on the host for HTTPS. When set, vhosts also listen on 443 and port 80 redirects to HTTPS. |
| `systemd_service_proxy_httpd_tls_key` |  | Private key file on the host for HTTPS. |
| `systemd_service_proxy_httpd_certbot` | `False` | Get a Let's Encrypt certificate for every vhost (with systemd_service_certbot) and use it for HTTPS. |
| `systemd_service_proxy_httpd_certbot_email` |  | Contact for Let's Encrypt expiry warnings. |
| `systemd_service_proxy_httpd_certbot_cert_name` | `{{ inventory_hostname }}` | Name of the Let's Encrypt certificate. Defaults to the inventory hostname. |
| `systemd_service_proxy_httpd_certbot_extra_domains` | `[]` | Extra domains for the certificate, besides the vhosts' server names. |
| `systemd_service_proxy_httpd_certbot_http_port` | `9080` | Port on 127.0.0.1 that certbot answers challenges on. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.systemd_service_proxy_httpd
      vars:
        systemd_service_proxy_httpd_vhosts:
          - server_name: app.example.com
            upstream: http://127.0.0.1:8080/
        systemd_service_proxy_httpd_certbot: true
        systemd_service_proxy_httpd_certbot_email: admin@example.com
        systemd_service_proxy_httpd_extra_templates:
          - src: httpd/index.html.j2
            dest: /var/www/html/index.html
```
