# systemd_service_proxy_haproxy

Installs haproxy (on the host) as a name-based reverse proxy for local
services. An approved alternative to [podman_app_proxy_nginx](../podman_app_proxy_nginx),
with the same vhost options. Replaces the old `systemd_service_haproxy` role.

- Each entry in `systemd_service_proxy_haproxy_vhosts` gets a backend, chosen
  by the request's `Host` header. Websockets are passed through.
- Every [podman_app](../podman_app) app on the host with a
  `podman_app_external_address` also gets one
  (`systemd_service_proxy_haproxy_podman_apps`). Run this role after them, in
  the same play.
- Stats (`/stats`) and Prometheus metrics (`/metrics`) are served on
  `127.0.0.1:8404` (`systemd_service_proxy_haproxy_stats_bind`).
- The config is checked with `haproxy -c` before being written, and changes
  trigger a graceful reload.

For a hand-written config instead, set `systemd_service_proxy_haproxy_cfg_file`
to your own template; the other options are then ignored.

## HTTPS

Plain HTTP on port 80 by default. For HTTPS, either:

- set `systemd_service_proxy_haproxy_tls_pem` to a PEM file already on the host
  holding the certificate chain and private key, or
- set `systemd_service_proxy_haproxy_certbot: true` to get a Let's Encrypt
  certificate covering every vhost, with [systemd_service_certbot](../systemd_service_certbot).
  The PEM is assembled into `/etc/haproxy/certs/` on issue and renewal. On the
  first run haproxy starts as HTTP only, so the challenge can be answered, and
  switches to HTTPS once the certificate exists.

With HTTPS, port 80 redirects to 443. Set `tls: false` on a vhost to keep it
HTTP only.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `systemd_service_proxy_haproxy_cfg_file` |  | A whole haproxy.cfg template of your own, found via the playbook search path. When set, it is used as is and the other options are ignored. |
| `systemd_service_proxy_haproxy_vhosts` | `[]` | Reverse proxy vhosts. Keys are server_name and upstream, plus optional tls (default true). Only the host and port of upstream are used. |
| `systemd_service_proxy_haproxy_podman_apps` | `True` | Also add a vhost for each podman_app app on this host that sets podman_app_external_address. Run this role after the podman_app roles in the same play, as it reads the podman_app_external_apps fact they set. |
| `systemd_service_proxy_haproxy_tls_pem` |  | PEM file on the host holding the certificate chain and private key, for HTTPS. When set, port 80 redirects to HTTPS. |
| `systemd_service_proxy_haproxy_certbot` | `False` | Get a Let's Encrypt certificate for every vhost (with systemd_service_certbot) and use it for HTTPS. |
| `systemd_service_proxy_haproxy_certbot_email` |  | Contact for Let's Encrypt expiry warnings. |
| `systemd_service_proxy_haproxy_certbot_cert_name` | `{{ inventory_hostname }}` | Name of the Let's Encrypt certificate. Defaults to the inventory hostname. |
| `systemd_service_proxy_haproxy_certbot_extra_domains` | `[]` | Extra domains for the certificate, besides the vhosts' server names. |
| `systemd_service_proxy_haproxy_certbot_http_port` | `9080` | Port on 127.0.0.1 that certbot answers challenges on. |
| `systemd_service_proxy_haproxy_stats_bind` | `127.0.0.1:8404` | Address for stats (/stats) and Prometheus metrics (/metrics). Empty turns it off. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.systemd_service_proxy_haproxy
      vars:
        systemd_service_proxy_haproxy_vhosts:
          - server_name: app.example.com
            upstream: http://127.0.0.1:8080/
        systemd_service_proxy_haproxy_certbot: true
        systemd_service_proxy_haproxy_certbot_email: admin@example.com
```
