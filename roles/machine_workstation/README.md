# machine_workstation

My desktop workstation
## Variables
| Variable | Default |
|----------|---------|
| `machine_workstation_graphical` | False |


## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.machine_workstation
      vars:
        machine_workstation_graphical: False
```
