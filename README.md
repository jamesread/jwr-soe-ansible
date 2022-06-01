# jwr-ansible-soe

An Ansible [collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) of roles for [James Read's](http://jread.com/) (JWR) [Standard Operating Environment](https://en.wikipedia.org/wiki/Standard_Operating_Environment) (SOE). 

This is published on Ansible Galaxy as [jamesread.soe](https://galaxy.ansible.com/jamesread/soe). 

## Roles

### infra layer

* Nothing here yet

### machine layer

*  jamesread.soe.[machine_jenkins_slave](roles/machine_jenkins_slave) - Installs a Jenkins slave.
*  jamesread.soe.[machine_k8s](roles/machine_k8s) - Install a k8s node (could be a control/worker).
*  jamesread.soe.[machine_kiosk](roles/machine_kiosk) - My heads up display (kiosk)
*  jamesread.soe.[machine_podman](roles/machine_podman) - Installs podman.
*  jamesread.soe.[machine_sysadmin_utils](roles/machine_sysadmin_utils) - Various utils used for sysadmins.
*  jamesread.soe.[machine_wol](roles/machine_wol) - Enable Wake on LAN.
*  jamesread.soe.[machine_workstation](roles/machine_workstation) - My desktop workstation

### workload layer

*  jamesread.soe.[podman_dashboard](roles/podman_dashboard) - Installs a Dashboard container.
*  jamesread.soe.[podman_efk](roles/podman_efk) - Installs a EFK stack.
*  jamesread.soe.[podman_grafana](roles/podman_grafana) - Installs a Grafana container.
*  jamesread.soe.[podman_loki](roles/podman_loki) - Install loki as a podman container.
*  jamesread.soe.[podman_openhab](roles/podman_openhab) - Installs a OpenHAB container.
*  jamesread.soe.[podman_prom_gcal_exporter](roles/podman_prom_gcal_exporter) - Installs a Google Calendar Prometheus exporter.
*  jamesread.soe.[podman_prom_gmail_exporter](roles/podman_prom_gmail_exporter) - Installs a gmail exporter container.
*  jamesread.soe.[podman_prometheus](roles/podman_prometheus) - Installs a Prometheus container.
*  jamesread.soe.[podman_promtail](roles/podman_promtail) - Installs a promtail container.
*  jamesread.soe.[podman_traefik](roles/podman_traefik) - Installs a traefik container.
*  jamesread.soe.[systemd_service_apachephp](roles/systemd_service_apachephp) - Installs httpd.
*  jamesread.soe.[systemd_service_condor](roles/systemd_service_condor) - Installs condor as a service.
*  jamesread.soe.[systemd_service_filebeat](roles/systemd_service_filebeat) - Installs a filebeat service.
*  jamesread.soe.[systemd_service_haproxy](roles/systemd_service_haproxy) - Installs haproxy as a service.
*  jamesread.soe.[systemd_service_jenkins](roles/systemd_service_jenkins) - Installs jenkins as a service.
*  jamesread.soe.[systemd_service_journalbeat](roles/systemd_service_journalbeat) - Installs a journalbeat systemd service.
*  jamesread.soe.[systemd_service_kvmlibvirt](roles/systemd_service_kvmlibvirt) - Installs kvm, libvirt and essential virt tools.

### misc layer

*  jamesread.soe.[common](roles/common) - Common/baseline config. Prometheus node exporter, sshd, SMART, etc.
*  jamesread.soe.[libvirt_vm](roles/libvirt_vm) - Creates a libvirtvm.

## Usage 

Install the collection like this

    ansible-galaxy collection install jamesread.soe

Create a playbook like this

    #!/usr/bin/env ansible-playbook

    - hosts: 
        - all
      roles: 
        - name: jamesread.soe.common
          myVar: foobar

## Principles

* Separation of data (mostly config files) and reusable code (roles). 
* Separation of layers (ie, containers should not depend on an OS thing)

## Layers

1. Infra: (nothing here yet)
2. OS Configuration (Physical/Virtual machine) - `machine_`
3. OS Apps: `systemd_service_*`
4. OS Containers: `podman_*`

## Notes

No `site.yml`. I started off with this, but honestly have no idea where it's
supposed to fit if you're trying to promote role re-use and separation of
data/code. 
