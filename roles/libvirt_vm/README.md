# libvirt_vm

Creates a libvirtvm.
## Variables
| Variable | Default |
|----------|---------|
| `baseImageDirectory` | /jwrFs/Software/PC/OS/ |
| `baseImageFilename` | Fedora-Cloud-Base-35-1.2.x86_64.qcow2 |
| `vmTitle` | untitled |
| `nameFormat` | {{ vmTitle }}-%02x |
| `count` | 1 |
| `diskSize` | 8 |
| `ramMb` | 4096 |
| `vcpuCount` | 2 |
| `useCloudInit` | False |
| `rawDisk` | 0 |
| `vmCustomize` | cloud-init |
| `extraVmCustomize` | None |
| `extraVirtInstall` | None |


## Example usage in a playbook

```
- hosts: [myserver]
  roles
    - roles: jamesread.soe.libvirt_vm
      vars:
        baseImageDirectory: /jwrFs/Software/PC/OS/
        baseImageFilename: Fedora-Cloud-Base-35-1.2.x86_64.qcow2
        vmTitle: untitled
        nameFormat: {{ vmTitle }}-%02x
        count: 1
        diskSize: 8
        ramMb: 4096
        vcpuCount: 2
        useCloudInit: False
        rawDisk: 0
        vmCustomize: cloud-init
        extraVmCustomize: None
        extraVirtInstall: None
```
