# systemd_service_httpd_proxy

Installs httpd as a name-based reverse proxy for local services (plain HTTP on :80, e.g. behind Cloudflare).

- Each entry in `systemd_service_httpd_proxy_vhosts` becomes `<conf_dir>/<server_name>.conf`, proxying `/` to `upstream`.
- Bespoke vhosts and landing pages go in `systemd_service_httpd_proxy_extra_templates`. Their `src` resolves via the playbook search path, so the templates stay in the environment repo.
- Config changes trigger a graceful reload.

Unlike `systemd_service_apachephp`, this role installs no PHP and does not touch firewalld.

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.systemd_service_httpd_proxy
      vars:
        systemd_service_httpd_proxy_vhosts:
          - server_name: app.example.com
            upstream: http://127.0.0.1:8080/
        systemd_service_httpd_proxy_extra_templates:
          - src: httpd/index.html.j2
            dest: /var/www/html/index.html
```
