import os
import io
import sys
import yaml


def find_config():
    config = None
    env = os.getenv('ENVIRONMENT', 'development')

    if env != 'test':
        try:
            with io.open('mo.yml', 'r') as stream:
                config = yaml.load(stream)
        except IOError:
            sys.exit('Cannot open mo.yml')

    return config
