# jwr-ansible-soe

An Ansible [collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) of roles for [James Read's](http://jread.com/) (JWR) [Standard Operating Environment](https://en.wikipedia.org/wiki/Standard_Operating_Environment) (SOE). 

This is published on Ansible Galaxy as "[https://galaxy.ansible.com/jamesread/soe](jamesread.soe)". 

## Roles

*  jamesread.soe.[cifs](roles/cifs) [[README](roles/cifs/README.md)] - Mount a CIFS share.
*  jamesread.soe.[common](roles/common) [[README](roles/common/README.md)] - Common/baseline config. Prometheus node exporter, sshd, SMART, etc.
*  jamesread.soe.[containerhost_podman](roles/containerhost_podman) [[README](roles/containerhost_podman/README.md)] - Installs podman.
*  jamesread.soe.[machine_jenkins_slave](roles/machine_jenkins_slave) [[README](roles/machine_jenkins_slave/README.md)] - Installs a Jenkins slave.
*  jamesread.soe.[machine_k8s](roles/machine_k8s) [[README](roles/machine_k8s/README.md)] - Install a k8s node (could be a control/worker).
*  jamesread.soe.[machine_kiosk](roles/machine_kiosk) [[README](roles/machine_kiosk/README.md)] - My heads up display (kiosk)
*  jamesread.soe.[machine_workstation](roles/machine_workstation) [[README](roles/machine_workstation/README.md)] - My desktop workstation
*  jamesread.soe.[podman_dashboard](roles/podman_dashboard) [[README](roles/podman_dashboard/README.md)] - Installs a Grafana container.
*  jamesread.soe.[podman_efk](roles/podman_efk) [[README](roles/podman_efk/README.md)] - Installs a EFK stack.
*  jamesread.soe.[podman_grafana](roles/podman_grafana) [[README](roles/podman_grafana/README.md)] - Installs a Grafana container.
*  jamesread.soe.[podman_loki](roles/podman_loki) [[README](roles/podman_loki/README.md)] - Install loki as a podman container.
*  jamesread.soe.[podman_openhab](roles/podman_openhab) [[README](roles/podman_openhab/README.md)] - Installs a OpenHAB container.
*  jamesread.soe.[podman_prom_gcal_exporter](roles/podman_prom_gcal_exporter) [[README](roles/podman_prom_gcal_exporter/README.md)] - Installs a Google Calendar Prometheus exporter.
*  jamesread.soe.[podman_prom_gmail_exporter](roles/podman_prom_gmail_exporter) [[README](roles/podman_prom_gmail_exporter/README.md)] - Installs a gmail exporter container.
*  jamesread.soe.[podman_prometheus](roles/podman_prometheus) [[README](roles/podman_prometheus/README.md)] - Installs a Prometheus container.
*  jamesread.soe.[podman_promtail](roles/podman_promtail) [[README](roles/podman_promtail/README.md)] - Installs a promtail container.
*  jamesread.soe.[podman_traefik](roles/podman_traefik) [[README](roles/podman_traefik/README.md)] - Installs a traefik container.
*  jamesread.soe.[systemd_kvm_hypervisor](roles/systemd_kvm_hypervisor) [[README](roles/systemd_kvm_hypervisor/README.md)] - Installs KVM, libvirt, etc.
*  jamesread.soe.[systemd_service_apachephp](roles/systemd_service_apachephp) [[README](roles/systemd_service_apachephp/README.md)] - Installs httpd.
*  jamesread.soe.[systemd_service_condor](roles/systemd_service_condor) [[README](roles/systemd_service_condor/README.md)] - Installs condor as a service.
*  jamesread.soe.[systemd_service_filebeat](roles/systemd_service_filebeat) [[README](roles/systemd_service_filebeat/README.md)] - Installs a filebeat service.
*  jamesread.soe.[systemd_service_haproxy](roles/systemd_service_haproxy) [[README](roles/systemd_service_haproxy/README.md)] - Installs haproxy as a service.
*  jamesread.soe.[systemd_service_jenkins](roles/systemd_service_jenkins) [[README](roles/systemd_service_jenkins/README.md)] - Installs jenkins as a service.
*  jamesread.soe.[systemd_service_journalbeat](roles/systemd_service_journalbeat) [[README](roles/systemd_service_journalbeat/README.md)] - Installs a journalbeat systemd service.
*  jamesread.soe.[systemd_service_kvmlibvirt](roles/systemd_service_kvmlibvirt) [[README](roles/systemd_service_kvmlibvirt/README.md)] - Installs kvm, libvirt and essential virt tools.

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

# Layers

1. Infra: (nothing here yet)
2. OS Configuration (Physical/Virtual machine) - `machine_`
3. OS Apps: `systemd_service_*`
4. OS Containers: `podman_*`

# Notes

No `site.yml`. I started off with this, but honestly have no idea where it's
supposed to fit if you're trying to promote role re-use and separation of
data/code. 
