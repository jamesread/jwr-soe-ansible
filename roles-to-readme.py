#!/usr/bin/env python

import os
import os.path
import yaml

import markdown

class AnsibleRole:
    description = "?"
    url = "?"
    directory = ""
    name = "?"
    variables = list()

class RoleVariable:
    name = ""
    default = ""

def get_role_layer(name):
    if "machine_" in name: return "machine"
    if "systemd_service" in name: return "workload"
    if "podman_" in name: return "workload"

    return "misc"

def extract_roles():
    roles = list()

    for d in sorted(os.listdir("roles")):
        r = AnsibleRole()
        r.directory = "roles/" + d + "/"
        r.name = d
        r.url = "jamesread.soe.[" + d + "](roles/" + d + ")"
        r.readmeLink = "[[README](roles/" + d + "/README.md)]"
        r.layer = get_role_layer(r.name)


        try:
            with open(os.path.join("roles", d, 'meta/main.yml'), 'r') as role_file:
                role_md = yaml.safe_load(role_file)

                r.description = role_md['galaxy_info']['description']

        except Exception as e:
            print(d, str(e))

        r.variables = extract_role_variables(r)

        roles.append(r)

    return roles

def extract_role_variables(r):
    ret = list()

    try:
        with open(os.path.join(r.directory, 'defaults/main.yml'), 'r') as defaults_file:
            defaults_content = yaml.safe_load(defaults_file)

            for v in defaults_content:
                v2 = RoleVariable()
                v2.name = v
                v2.default = str(defaults_content[v])

                ret.append(v2)

    except FileNotFoundError:
        pass
    except Exception as e:
        print(e, str(e))

    return ret

def roles_to_markdown_overview(roles):
    for layer in ["infra", "machine", "workload", "misc"]:
        print("\n### " + layer + " layer\n")

        for r in roles:
            if r.layer == layer:
                print("* ", r.url, "-", r.description)

def roles_to_role_readmes(roles):
    for r in roles:
        with open(os.path.join(r.directory, "README.md"), 'w') as role_readme:
            role_readme.write(generate_role_readme(r))


def generate_role_readme(r):
    ret = ""
    ret += "# " + r.name + "\n\n"
    ret += r.description + "\n"
    ret += "## Variables\n"

    if len(r.variables) == 0:
        ret += "This role does not have any variables.\n"
    else:
        ret += "| Variable | Default |\n"
        ret += "|----------|---------|\n"

        for var in r.variables:
            ret += "| `" + var.name + "` | " + var.default + " |\n"


    ret += "\n\n## Example usage in a playbook\n\n"
    ret += "```yaml\n"
    ret += "- hosts: [myserver]\n"
    ret += "  roles:\n"
    ret += "    - role: jamesread.soe." + r.name + "\n"

    if len(r.variables) > 0:
        ret += "      vars:\n"

        for var in r.variables:
            ret += "        " + var.name + ": " + var.default + "\n"

    ret += "```\n"

    return ret

if __name__ == "__main__":
    roles = extract_roles()

    roles_to_markdown_overview(roles)
    roles_to_role_readmes(roles)
