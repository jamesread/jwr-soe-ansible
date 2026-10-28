# infra_libvirt_vm

Creates a libvirtvm.
## Variables
| Variable | Default |
|----------|---------|
| `infra_libvirt_vm_base_image_directory` | /jwrFs/Software/PC/OS/ |
| `infra_libvirt_vm_base_image_filename` | Fedora-Cloud-Base-35-1.2.x86_64.qcow2 |
| `infra_libvirt_vm_title` | untitled |
| `infra_libvirt_vm_name_format` | {{ infra_libvirt_vm_title }}-%02x |
| `infra_libvirt_vm_count` | 1 |
| `infra_libvirt_vm_disk_size` | 8 |
| `infra_libvirt_vm_ram_mb` | 4096 |
| `infra_libvirt_vm_vcpu_count` | 2 |
| `infra_libvirt_vm_use_cloud_init` | False |
| `infra_libvirt_vm_raw_disk` | 0 |
| `infra_libvirt_vm_customize` | cloud-init |
| `infra_libvirt_vm_extra_customize` | None |
| `infra_libvirt_vm_extra_virt_install` | None |
| `infra_libvirt_vm_root_password` |  |
| `infra_libvirt_vm_ssh_authorized_keys` | [] |
| `infra_libvirt_vm_ssh_inject_key_file` | /root/.ssh/id_rsa.pub |
| `infra_libvirt_vm_ssh_pwauth` | False |
| `infra_libvirt_vm_permit_root_login` | False |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.infra_libvirt_vm
      vars:
        infra_libvirt_vm_base_image_directory: /jwrFs/Software/PC/OS/
        infra_libvirt_vm_base_image_filename: Fedora-Cloud-Base-35-1.2.x86_64.qcow2
        infra_libvirt_vm_title: untitled
        infra_libvirt_vm_name_format: {{ infra_libvirt_vm_title }}-%02x
        infra_libvirt_vm_count: 1
        infra_libvirt_vm_disk_size: 8
        infra_libvirt_vm_ram_mb: 4096
        infra_libvirt_vm_vcpu_count: 2
        infra_libvirt_vm_use_cloud_init: False
        infra_libvirt_vm_raw_disk: 0
        infra_libvirt_vm_customize: cloud-init
        infra_libvirt_vm_extra_customize: None
        infra_libvirt_vm_extra_virt_install: None
        infra_libvirt_vm_root_password:
        infra_libvirt_vm_ssh_authorized_keys: []
        infra_libvirt_vm_ssh_inject_key_file: /root/.ssh/id_rsa.pub
        infra_libvirt_vm_ssh_pwauth: False
        infra_libvirt_vm_permit_root_login: False
```
