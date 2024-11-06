# libvirt_vm

Creates a libvirtvm.
## Variables
| Variable | Default |
|----------|---------|
| `base_image_directory` | /jwrFs/Software/PC/OS/ |
| `base_image_filename` | Fedora-Cloud-Base-35-1.2.x86_64.qcow2 |
| `vm_title` | untitled |
| `name_format` | {{ vmTitle }}-%02x |
| `count` | 1 |
| `disk_size` | 8 |
| `ram_mb` | 4096 |
| `vcpu_count` | 2 |
| `use_cloud_init` | False |
| `raw_disk` | 0 |
| `vm_customize` | cloud-init |
| `extra_vm_customize` | None |
| `extra_virt_install` | None |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles
    - roles: jamesread.soe.libvirt_vm
      vars:
        base_image_directory: /jwrFs/Software/PC/OS/
        base_image_filename: Fedora-Cloud-Base-35-1.2.x86_64.qcow2
        vm_title: untitled
        name_format: {{ vmTitle }}-%02x
        count: 1
        disk_size: 8
        ram_mb: 4096
        vcpu_count: 2
        use_cloud_init: False
        raw_disk: 0
        vm_customize: cloud-init
        extra_vm_customize: None
        extra_virt_install: None
```
