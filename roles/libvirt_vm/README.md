# libvirt_vm

Creates a libvirtvm.
## Variables
* `baseImageDirectory` (default: /jwrFs/Software/PC/OS/)
* `baseImageFilename` (default: Fedora-Cloud-Base-35-1.2.x86_64.qcow2)
* `vmTitle` (default: untitled)
* `nameFormat` (default: {{ vmTitle }}-%02x)
* `count` (default: 1)
* `diskSize` (default: 8)
* `ramMb` (default: 4096)
* `vcpuCount` (default: 2)
* `useCloudInit` (default: False)
* `rawDisk` (default: 0)
* `vmCustomize` (default: cloud-init)
* `extraVmCustomize` (default: None)
* `extraVirtInstall` (default: None)
