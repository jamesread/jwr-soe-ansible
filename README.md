# jwr-ansible-soe

An Ansible [collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) of roles for [James Read's](http://jread.com/) (JWR) [Standard Operating Environment](https://en.wikipedia.org/wiki/Standard_Operating_Environment) (SOE). 

## Usage 

Create a playbook like this;

----
    #!/usr/bin/env ansible-playbook
    
    - hosts: 
        - group_common
      roles: 
        - name: jamesread.soe.common
          myVar: foobar
----

## Principals

* Separation of data (mostly config files) and reusable code (roles). 
* Separation of layers (ie, containers should not depend on an OS thing)

# Layers;

1. Infra: (nothing here yet)
2. OS Configuration (Physical/Virtual machine) - `machine_`
3. OS Apps: `systemd_service_*`
4. OS Containers: `podman_*`

# Notes

No `site.yml`. I started off with this, but honestly have no idea where it's
supposed to fit if you're trying to promote role re-use and separation of
data/code. 
