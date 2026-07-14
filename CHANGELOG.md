# CHANGELOG

## 2.0.0

Breaking change: all role default variables and ephemeral task variables now use
the ansible-lint `role_name_` prefix. Update playbooks that override role vars.

### Security and correctness

- `libvirt_vm`: removed hardcoded root password and SSH public key; require
  `libvirt_vm_ssh_authorized_keys` and/or `libvirt_vm_root_password` (Vault).
  Password auth and root login default to off.
- `libvirt_vm`: fixed cloud-init path (copy base image, generate cloud-init ISO
  via `create-cloud-init.yml`).
- `podman_efk`: removed hardcoded `changeme` / encryption key; require
  `podman_efk_elastic_password` and `podman_efk_kibana_encryption_key`.
- `systemd_service_jenkins`: no longer prints the initial admin password.
- `systemd_service_journalbeat`: fixed handler notify casing so restarts run.
- Collection now depends on `community.general` and `ansible.posix`.
- Added `meta/argument_specs.yml` for roles that define defaults.

### Public variable renames

| Role | Old | New |
|------|-----|-----|
| `libvirt_vm` | `base_image_directory` | `libvirt_vm_base_image_directory` |
| `libvirt_vm` | `base_image_filename` | `libvirt_vm_base_image_filename` |
| `libvirt_vm` | `vm_title` | `libvirt_vm_title` |
| `libvirt_vm` | `name_format` | `libvirt_vm_name_format` |
| `libvirt_vm` | `count` | `libvirt_vm_count` |
| `libvirt_vm` | `disk_size` | `libvirt_vm_disk_size` |
| `libvirt_vm` | `ram_mb` | `libvirt_vm_ram_mb` |
| `libvirt_vm` | `vcpu_count` | `libvirt_vm_vcpu_count` |
| `libvirt_vm` | `use_cloud_init` | `libvirt_vm_use_cloud_init` |
| `libvirt_vm` | `raw_disk` | `libvirt_vm_raw_disk` |
| `libvirt_vm` | `vm_customize` | `libvirt_vm_customize` |
| `libvirt_vm` | `extra_vm_customize` | `libvirt_vm_extra_customize` |
| `libvirt_vm` | `extra_virt_install` | `libvirt_vm_extra_virt_install` |
| `machine_podman` | `cfg_traefik_installed` | `machine_podman_traefik_installed` |
| `machine_podman` | `cfg_haproxy` | `machine_podman_haproxy_cfg` |
| `podman_dashboard` | `dashboard_volume` | `podman_dashboard_volume` |
| `podman_dashboard` | `dashboard_config` | `podman_dashboard_config` |
| `podman_grafana` | `cfg_grafana_installed` | `podman_grafana_installed` |
| `podman_grafana` | `container_podman_volume` | `podman_grafana_volume` |
| `podman_prometheus` | `cfg_file` | `podman_prometheus_cfg_file` |
| `podman_prometheus` | `alert_file` | `podman_prometheus_alert_file` |
| `podman_prom_gcal_exporter` | `config_file` | `podman_prom_gcal_exporter_config_file` |
| `podman_prom_gcal_exporter` | `secret_file` | `podman_prom_gcal_exporter_secret_file` |
| `podman_prom_gmail_exporter` | `config_file` | `podman_prom_gmail_exporter_config_file` |
| `podman_prom_gmail_exporter` | `secret_file` | `podman_prom_gmail_exporter_secret_file` |
| `podman_traefik` | `traefik_volume` | `podman_traefik_volume` |
| `podman_traefik` | `traefik_config` | `podman_traefik_config` |
| `systemd_service_haproxy` | `cfg_file` | `systemd_service_haproxy_cfg_file` |

`podman_prom_gmail_exporter` previously used undeclared `config_file` /
`secret_file`; defaults were added with the new names.
