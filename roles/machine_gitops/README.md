# machine_gitops

GitOps by push: the host keeps a bare git repo, and pushing to its branch
deploys. The `post-receive` hook:

1. refreshes a deploy checkout (`machine_gitops_checkout_dir`) to the pushed
   branch, discarding any local edits there;
2. installs the collections the repo requires
   (`machine_gitops_requirements`, upgraded within their version ranges), so a
   push that bumps `jamesread.soe` takes effect;
3. runs `machine_gitops_command` in the checkout, eg
   `ansible-playbook ansible/playbooks/site.yml -c local -l myhost`.

Deploys run one at a time, and their output is shown to whoever pushed. Add the
host as a remote and push to it:

```bash
git remote add myhost root@myhost:/srv/git/example.com.git
git push myhost main
```

Tools like OliveTin can run playbooks from the same checkout.

<!-- BEGIN GENERATED VARIABLES -->

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `machine_gitops_name` | (required) | Name of the site repo, eg example.com. Used in the default paths. |
| `machine_gitops_repo_dir` | `/srv/git/{{ machine_gitops_name }}.git` | Bare repo on this host to push to. Defaults to /srv/git/<name>.git. |
| `machine_gitops_checkout_dir` | `/srv/gitops/{{ machine_gitops_name }}` | Deploy checkout, refreshed on every push (local edits there are discarded). Defaults to /srv/gitops/<name>. |
| `machine_gitops_branch` | `main` | Branch that deploys. |
| `machine_gitops_command` |  | Command run in the checkout after each push, eg ansible-playbook ansible/playbooks/site.yml -c local -l myhost. Empty only refreshes the checkout. |
| `machine_gitops_requirements` | `ansible/collections/requirements.yml` | Collections requirements file in the repo. If it exists, the collections are installed (upgraded within their version ranges) before the command. Empty skips this. |
| `machine_gitops_collections_path` | `ansible/collections` | Where in the checkout to install the collections. |
| `machine_gitops_packages` | `[git, ansible-core]` | Packages the hook needs. |

<!-- END GENERATED VARIABLES -->

## Example usage in a playbook

```yaml
- hosts: [myhost]
  roles:
    - role: jamesread.soe.machine_gitops
      vars:
        machine_gitops_name: example.com
        machine_gitops_command: ansible-playbook ansible/playbooks/site.yml -c local -l myhost
```
