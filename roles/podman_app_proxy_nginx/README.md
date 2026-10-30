# podman_app_proxy_nginx

Runs nginx in a container, using [podman_app](../podman_app), as a name-based
reverse proxy for local services. This is the recommended proxy; host
[httpd](../systemd_service_proxy_httpd) and [haproxy](../systemd_service_proxy_haproxy)
are approved alternatives with the same vhost options.

The container (`proxy-nginx`) is rootful and uses the host network, so it can
bind ports 80 and 443 and reach apps published on `127.0.0.1`. Nothing is
installed on the host apart from podman.

- Each entry in `podman_app_proxy_nginx_vhosts` becomes a `server` block
  proxying `/` (including websockets) to `upstream`, with the usual
  `X-Forwarded-*` headers.
- Every [podman_app](../podman_app) app on the host with a
  `podman_app_external_address` also gets one (`podman_app_proxy_nginx_podman_apps`).
  Run this role after them, in the same play.
- Requests for a hostname with no vhost are turned away
  (`podman_app_proxy_nginx_default_server`).
- The config is generated into `/etc/proxy-nginx/conf.d/proxy.conf`, checked
  with `nginx -t`, and applied with a graceful reload (SIGHUP).

## HTTPS

Plain HTTP on port 80 by default (eg behind Cloudflare). For HTTPS, either:

- set `podman_app_proxy_nginx_tls_cert` and `_tls_key` to a certificate
  already on the host (eg a wildcard certificate), or
- set `podman_app_proxy_nginx_certbot: true` to get a Let's Encrypt
  certificate covering every vhost, with [systemd_service_certbot](../systemd_service_certbot).
  On the first run vhosts start as HTTP only, so the challenge can be answered,
  and switch to HTTPS once the certificate exists. Renewals reload nginx.

The certificate and key are copied into `/etc/proxy-nginx/tls/`, as the
container cannot read them elsewhere on the host. With HTTPS, vhosts listen on
443 (with HTTP/2) and port 80 redirects to it. Set `tls: false` on a vhost to
keep it HTTP only.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `podman_app_proxy_nginx_image` | `docker.io/library/nginx:stable-alpine` | nginx container image. |
| `podman_app_proxy_nginx_dir` | `/etc/proxy-nginx` | Host directory for the generated config (in conf.d/) and TLS files (in tls/). |
| `podman_app_proxy_nginx_vhosts` | `[]` | Reverse proxy vhosts. Keys are server_name and upstream, plus optional tls (default true) and extra (raw nginx lines for the vhost's location /). |
| `podman_app_proxy_nginx_podman_apps` | `True` | Also add a vhost for each podman_app app on this host that sets podman_app_external_address. Run this role after the podman_app roles in the same play, as it reads the podman_app_external_apps fact they set. |
| `podman_app_proxy_nginx_tls_cert` |  | Certificate (chain) file on the host for HTTPS. When set, vhosts also listen on 443 and port 80 redirects to HTTPS. |
| `podman_app_proxy_nginx_tls_key` |  | Private key file on the host for HTTPS. |
| `podman_app_proxy_nginx_certbot` | `False` | Get a Let's Encrypt certificate for every vhost (with systemd_service_certbot) and use it for HTTPS. |
| `podman_app_proxy_nginx_certbot_email` |  | Contact for Let's Encrypt expiry warnings. |
| `podman_app_proxy_nginx_certbot_cert_name` | `{{ inventory_hostname }}` | Name of the Let's Encrypt certificate. Defaults to the inventory hostname. |
| `podman_app_proxy_nginx_certbot_extra_domains` | `[]` | Extra domains for the certificate, besides the vhosts' server names. |
| `podman_app_proxy_nginx_certbot_http_port` | `9080` | Port on 127.0.0.1 that certbot answers challenges on. |
| `podman_app_proxy_nginx_default_server` | `True` | Turn away requests for hostnames with no vhost, rather than serving the first vhost. |
| `podman_app_proxy_nginx_ipv6` | `True` | Also listen on IPv6. Turn off on hosts with IPv6 disabled. |
| `podman_app_proxy_nginx_client_max_body_size` | `100m` | Largest request body (eg upload) allowed. |
| `podman_app_proxy_nginx_extra_conf` |  | Raw nginx config added to the http context, eg extra server blocks. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_app
      vars:
        podman_app_name: japella
        podman_app_image: ghcr.io/jamesread/japella:latest
        podman_app_ports: ['127.0.0.1:8089:8080']
        podman_app_external_address: japella.example.com

    - role: jamesread.soe.podman_app_proxy_nginx
      vars:
        podman_app_proxy_nginx_vhosts:
          - server_name: ot.example.com
            upstream: http://127.0.0.1:1337/
        podman_app_proxy_nginx_certbot: true
        podman_app_proxy_nginx_certbot_email: admin@example.com
```
