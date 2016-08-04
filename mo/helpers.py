import os
import io
import sys
import yaml
from subprocess import call


def find_config():
    """Finds the configuration file for this project, and returns it
    """
    config = None
    env = os.getenv('ENVIRONMENT', 'production')

    if env != 'test':
        try:
            with io.open('mo.yml', 'r') as stream:
                config = yaml.load(stream)
        except IOError:
            sys.exit('Cannot open mo.yml')

    return config


def determine_toolbelt_status():

    code = 0
    env = os.getenv('ENVIRONMENT', 'production')

    if env != 'test':
        # surpress command output
        with open(os.devnull, "w") as f:
            try:
                code = call(["heroku", "--version"], stdout=f)
            except OSError:
                code = 1
    return code
