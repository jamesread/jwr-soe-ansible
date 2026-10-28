# podman_compose_apps

Deploys rootless Podman Compose apps from a list of compose templates, as `podman_compose_apps_user`.

For each entry in `podman_compose_apps_list`, the role:

1. creates `app_dir` and renders `compose_template` to `app_dir/docker-compose.yml`;
2. optionally renders `config_template` to `app_dir/config.yaml`, copies the `files_src` tree to `app_dir/files_dest/`, and renders `script_template` to `app_dir/script_dest` (mode 0755);
3. runs `compose up -d` inside a `timeout`.

Templates and files are site data. They resolve via the normal playbook search path (`<playbook_dir>/templates/`, `<playbook_dir>/files/`), so they stay in the environment repo.

Recreation:

- With `podman_compose_apps_pull_images: true` (the default), every app is pulled and `--force-recreate`d on each run. This is needed for `:latest` tags.
- Otherwise only apps whose rendered or copied files changed are recreated.

## Example usage in a playbook

```yaml
- hosts: [myserver]
  roles:
    - role: jamesread.soe.podman_compose_apps
      vars:
        podman_compose_apps_shared_network: apps
        podman_compose_apps_list:
          - name: wt
            app_dir: /home/app/wt
            compose_template: compose/wt/docker-compose.yml.j2
```
