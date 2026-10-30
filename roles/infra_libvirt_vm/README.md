# infra_libvirt_vm

Creates a libvirtvm.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `infra_libvirt_vm_base_image_directory` | `/jwrFs/Software/PC/OS/` | Directory containing the base qcow2 image. |
| `infra_libvirt_vm_base_image_filename` | `Fedora-Cloud-Base-35-1.2.x86_64.qcow2` | Base qcow2 image filename. |
| `infra_libvirt_vm_title` | `untitled` | Base name for the VM (and single-instance name). |
| `infra_libvirt_vm_name_format` | `{{ infra_libvirt_vm_title }}-%02x` | with_sequence format when creating multiple VMs. |
| `infra_libvirt_vm_count` | `1` | Number of VMs to create. |
| `infra_libvirt_vm_disk_size` | `8` | Extra disk size in GiB added with qemu-img resize. |
| `infra_libvirt_vm_ram_mb` | `4096` | Memory for the VM in MiB. |
| `infra_libvirt_vm_vcpu_count` | `2` | Number of vCPUs. |
| `infra_libvirt_vm_use_cloud_init` | `False` | Legacy flag; prefer infra_libvirt_vm_customize. |
| `infra_libvirt_vm_raw_disk` | `0` | Reserved for raw disk sizing (legacy). |
| `infra_libvirt_vm_customize` | `cloud-init` | How to customize the guest before virt-install. |
| `infra_libvirt_vm_extra_customize` |  | Extra arguments appended to virt-customize. |
| `infra_libvirt_vm_extra_virt_install` |  | Extra arguments appended to virt-install. |
| `infra_libvirt_vm_root_password` |  | Root password (set via Vault). Required for virt-customize; optional for cloud-init if SSH keys are set. |
| `infra_libvirt_vm_ssh_authorized_keys` | `[]` | SSH public keys injected via cloud-init. |
| `infra_libvirt_vm_ssh_inject_key_file` | `/root/.ssh/id_rsa.pub` | Host path to public key for virt-customize --ssh-inject. |
| `infra_libvirt_vm_ssh_pwauth` | `False` | Allow SSH password authentication in cloud-init guests. |
| `infra_libvirt_vm_permit_root_login` | `False` | Allow password root SSH login (when true). Otherwise prohibit-password. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.infra_libvirt_vm
```
