#!/usr/bin/env python
# Regenerates the generated parts of the READMEs, leaving hand-written docs alone:
#
# - README.md: the role list, between the GENERATED ROLES markers.
# - roles/*/README.md: the variables table, between the GENERATED VARIABLES
#   markers. A README without markers gets them added: replacing an old fully
#   generated "## Variables" section if there is one, or appended otherwise.
#   A missing README is created.
#
# Run it from the repository root after adding or changing a role.

import os
import os.path
import re
import yaml

ROLES_BEGIN = "<!-- BEGIN GENERATED ROLES -->"
ROLES_END = "<!-- END GENERATED ROLES -->"
VARS_BEGIN = "<!-- BEGIN GENERATED VARIABLES -->"
VARS_END = "<!-- END GENERATED VARIABLES -->"

LAYERS = ["infra", "machine", "workload", "misc"]


class AnsibleRole:
    def __init__(self, name):
        self.name = name
        self.directory = os.path.join("roles", name)
        self.description = "?"
        self.layer = get_role_layer(name)
        self.variables = []


class RoleVariable:
    def __init__(self, name, default, description=""):
        self.name = name
        self.default = default
        self.description = description


def get_role_layer(name):
    if name.startswith("infra_"):
        return "infra"
    if name.startswith("machine_"):
        return "machine"
    if name.startswith("systemd_service_") or name.startswith("podman_"):
        return "workload"

    return "misc"


def load_yaml(path):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}


def extract_roles():
    roles = []

    for d in sorted(os.listdir("roles")):
        r = AnsibleRole(d)

        meta = load_yaml(os.path.join(r.directory, "meta/main.yml"))
        r.description = meta.get("galaxy_info", {}).get("description", "?").strip()
        r.variables = extract_role_variables(r)

        roles.append(r)

    return roles


def describe(option):
    description = option.get("description", "")

    if isinstance(description, list):
        description = " ".join(description)

    return " ".join(str(description).split())


def extract_role_variables(r):
    # Prefer argument_specs (it has descriptions and required options), and add
    # any defaults it does not mention.
    specs = load_yaml(os.path.join(r.directory, "meta/argument_specs.yml"))
    options = specs.get("argument_specs", {}).get("main", {}).get("options", {}) or {}
    defaults = load_yaml(os.path.join(r.directory, "defaults/main.yml"))

    ret = []

    for name, option in options.items():
        if option.get("required"):
            default = "(required)"
        elif name in defaults:
            default = format_default(defaults[name])
        else:
            default = format_default(option.get("default", ""))

        ret.append(RoleVariable(name, default, describe(option)))

    for name, value in defaults.items():
        if name not in options:
            ret.append(RoleVariable(name, format_default(value)))

    return ret


def format_default(value):
    if value is None or value == "":
        return ""

    if isinstance(value, (list, dict)) and len(value) > 0:
        value = yaml.safe_dump(value, default_flow_style=True, width=1000).strip()

    return "`" + str(value).replace("|", "\\|") + "`"


def roles_markdown(roles):
    ret = ""

    for layer in LAYERS:
        ret += "\n### " + layer + " layer\n\n"

        for r in roles:
            if r.layer == layer:
                ret += "* jamesread.soe.[" + r.name + "](roles/" + r.name + ") - " + r.description + "\n"

    return ret


def variables_markdown(r):
    if len(r.variables) == 0:
        return "\n## Variables\n\nThis role does not have any variables.\n\n"

    ret = "\n## Variables\n\n"
    ret += "| Variable | Default | Description |\n"
    ret += "|----------|---------|-------------|\n"

    for var in r.variables:
        ret += "| `" + var.name + "` | " + var.default + " | " + var.description.replace("|", "\\|") + " |\n"

    return ret + "\n"


def replace_between(text, begin, end, content):
    pattern = re.compile(re.escape(begin) + ".*?" + re.escape(end), re.S)
    return pattern.sub(lambda _: begin + "\n" + content + end, text, count=1)


def update_top_readme(roles):
    with open("README.md", "r") as f:
        text = f.read()

    if ROLES_BEGIN not in text:
        print("README.md: no " + ROLES_BEGIN + " marker, not updated")
        return

    with open("README.md", "w") as f:
        f.write(replace_between(text, ROLES_BEGIN, ROLES_END, roles_markdown(roles) + "\n"))


def update_role_readme(r):
    path = os.path.join(r.directory, "README.md")
    block = VARS_BEGIN + "\n" + variables_markdown(r) + VARS_END

    try:
        with open(path, "r") as f:
            text = f.read()
    except FileNotFoundError:
        text = None

    if text is None:
        text = "# " + r.name + "\n\n" + r.description + "\n\n" + block + "\n" + example_markdown(r)
    elif VARS_BEGIN in text:
        text = replace_between(text, VARS_BEGIN, VARS_END, variables_markdown(r))
    elif "\n## Variables\n" in text:
        # An old fully generated README: replace its generated tail.
        text = text[: text.index("\n## Variables\n")].rstrip() + "\n\n" + block + "\n" + example_markdown(r)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"

    with open(path, "w") as f:
        f.write(text)


def example_markdown(r):
    ret = "\n## Example usage in a playbook\n\n"
    ret += "```yaml\n"
    ret += "- hosts: [myserver]\n"
    ret += "  roles:\n"
    ret += "    - role: jamesread.soe." + r.name + "\n"
    ret += "```\n"

    return ret


if __name__ == "__main__":
    roles = extract_roles()

    update_top_readme(roles)

    for r in roles:
        update_role_readme(r)
