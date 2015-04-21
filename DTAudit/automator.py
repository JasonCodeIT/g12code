from pipe import JSONPipe

import time
import os
import random
import json


def render(template, variables):
    lines = open(template, 'r').readlines()
    code = "".join(lines)

    for name, value in variables.items():
        if type(value) in [unicode, str]:
            code = code.replace("{{{ " + name + " }}}", value)
        else:
            code = code.replace("{{{ " + name + " }}}", json.dumps(value))

    return code


class automator(JSONPipe):
    """Generate selenium scripts that automatically validate given exploits.
    """

    def __init__(self, template1, template2):
        self.template1 = template1
        self.template2 = template2


    def process(self, incomings):
        """Generate the selenium script here.

        `incomings[0]` is a list of exploits to be validated.

        return : a list of paths to the generated selenium scripts
        """

        script_folder = "scripts" + str(int(time.time()))
        if not os.path.exists(script_folder):
            os.makedirs(script_folder)

        scripts = []

        # extract data from json file
        for exploit in incomings[0]:
            script_name = exploit["name"] + '.py'
            script_name += ".py"
            script_path = os.path.join(script_folder, script_name)

            script = open(script_path, "w+")

            if "app8" not in exploit['exploit'][0]['url']:
                code = render(self.template1, {"steps": exploit['exploit']})
            else:
                code = render(self.template2, {"steps": exploit['exploit']})

            script.write(code)
            script.close()

            scripts.append(script_path)

        return scripts
