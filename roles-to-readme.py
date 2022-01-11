#!/usr/bin/env python

import os
import os.path
import yaml

for d in sorted(os.listdir("roles")):
    description = "?"
    url = "jamesread.soe.[" + d + "](roles/" + d + ")"

    try:
        with open(os.path.join("roles", d, 'meta/main.yml'), 'r') as role_file:
            role_md = yaml.safe_load(role_file)

            description = role_md['galaxy_info']['description']

    except Exception as e: 
        print(d, str(e))

    print("* ", url, "-",  description)
