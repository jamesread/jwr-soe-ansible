# jamesread.soe Ansible Collection (jwr-soe-ansible)

An Ansible [collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) of roles for [James Read's](http://jread.com/) (JWR) [Standard Operating Environment](https://en.wikipedia.org/wiki/Standard_Operating_Environment) (SOE).

This is published on Ansible Galaxy as [jamesread.soe](https://galaxy.ansible.com/jamesread/soe).

## Roles

### infra layer

*  jamesread.soe.[infra_libvirt_vm](roles/infra_libvirt_vm) - Creates a libvirtvm.

### machine layer

*  jamesread.soe.[machine_k8s](roles/machine_k8s) - Install a k8s node (could be a control/worker).
*  jamesread.soe.[machine_kiosk](roles/machine_kiosk) - My heads up display (kiosk)
*  jamesread.soe.[machine_podman](roles/machine_podman) - Installs podman.
*  jamesread.soe.[machine_sysadmin_utils](roles/machine_sysadmin_utils) - Various utils used for sysadmins.
*  jamesread.soe.[machine_wol](roles/machine_wol) - Enable Wake on LAN.
*  jamesread.soe.[machine_workstation](roles/machine_workstation) - My desktop workstation

### workload layer

*  jamesread.soe.[podman_app](roles/podman_app) - Runs any container image as a systemd service, using a Podman quadlet.
*  jamesread.soe.[podman_app_grafana](roles/podman_app_grafana) - Runs Grafana as a systemd service (podman quadlet).
*  jamesread.soe.[podman_app_prometheus](roles/podman_app_prometheus) - Runs Prometheus as a systemd service (podman quadlet).
*  jamesread.soe.[podman_efk](roles/podman_efk) - Installs a EFK stack.
*  jamesread.soe.[podman_loki](roles/podman_loki) - Install loki as a podman container.
*  jamesread.soe.[podman_promtail](roles/podman_promtail) - Installs a promtail container.
*  jamesread.soe.[systemd_service_apachephp](roles/systemd_service_apachephp) - Installs httpd.
*  jamesread.soe.[systemd_service_filebeat](roles/systemd_service_filebeat) - Installs a filebeat service.
*  jamesread.soe.[systemd_service_haproxy](roles/systemd_service_haproxy) - Installs haproxy as a service.
*  jamesread.soe.[systemd_service_jenkins](roles/systemd_service_jenkins) - Installs jenkins as a service.
*  jamesread.soe.[systemd_service_journalbeat](roles/systemd_service_journalbeat) - Installs a journalbeat systemd service.
*  jamesread.soe.[systemd_service_kvmlibvirt](roles/systemd_service_kvmlibvirt) - Installs kvm, libvirt and essential virt tools.

### misc layer

*  jamesread.soe.[common](roles/common) - Common/baseline config. Prometheus node exporter, sshd, SMART, etc.

## Usage

Install the collection like this

    ansible-galaxy collection install jamesread.soe

Create a playbook like this

```yaml
#!/usr/bin/env ansible-playbook

- hosts:
	- all
  roles:
	- name: jamesread.soe.common
	  myVar: foobar
```

## Principles

* Separation of data (mostly config files) and reusable code (roles).
* Separation of layers (ie, containers should not depend on an OS thing)

## Layers

1. Infra (provisioning machines): `infra_*`
2. OS Configuration (Physical/Virtual machine) - `machine_`
3. OS Apps: `systemd_service_*`
4. OS Containers: `podman_*`. `podman_app` runs any image as a quadlet;
   `podman_app_*` roles are common apps built on it.

## Versioning and releases

Roles change in breaking ways (renames, removals, variable changes), so pin the
collection to a major version, eg `ansible-galaxy collection install 'jamesread.soe:>=5.0.0,<6.0.0'`.

Releases are fully automated with [semantic-release](https://semantic-release.gitbook.io/)
from [conventional commits](https://www.conventionalcommits.org/) on `master`.
Every push runs `ansible-lint` first, and only releases if it passes. A new
release creates a git tag, a [GitHub Release](https://github.com/jamesread/jwr-soe-ansible/releases)
with release notes, and publishes that version to Ansible Galaxy.

| Commit message | Release |
|----------------|---------|
| `fix: ...`, `perf: ...` | Patch |
| `feat: ...` | Minor |
| `feat!: ...`, `fix!: ...` (any type with `!`), or a `BREAKING CHANGE:` footer | Major |
| `docs:`, `chore:`, `refactor:`, `ci:`, `test:`, `style:`, `build:` | No release |

Anything that would break an existing playbook (removing or renaming a role or
a variable, changing a default's behaviour) must be marked breaking, eg:

```
feat!: move libvirt_vm to the infra layer as infra_libvirt_vm

BREAKING CHANGE: the role and all of its variables are renamed from
libvirt_vm_* to infra_libvirt_vm_*.
```

## Notes

No `site.yml`. I started off with this, but honestly have no idea where it's
supposed to fit if you're trying to promote role re-use and separation of
data/code.
