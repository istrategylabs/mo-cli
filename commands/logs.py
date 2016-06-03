
from errors import MalformedMoYaml
from errors import UnknownEnvironment
from subprocess import call
import click
import sys
import yaml
import io


def command_logs(env):
    '''This command proxies the tail log command from the heroku-toolbelt.
    Since mo apps utilize the mo.yml descriptor which should contain it\'s
    heroku app names, this command will remove the verbosity of the the native
    command for brevity'''

    try:
        # Open the mo.yml file
        # TODO: Search recursively until we get to the root of the project
        stream = io.open('mo.yml', 'r')
        data = yaml.load(stream)
        heroku_envs = data.get('heroku')

        # If there is no heroku section of the mo.yml file, raise an error
        if (heroku_envs is None):
            raise MalformedMoYaml('No heroku apps defined for this project')

        staging = heroku_envs.get('staging')
        production = heroku_envs.get('production')

        # Supported environments are staging and production
        if (env != 'staging' and env != 'production'):
            raise UnknownEnvironment("Unknown environment {0}".format(env))

        # If the specified (or default) environment is not configured, raise
        # an error
        if (env is 'production' and production is None):
            raise MalformedMoYaml('No production heroku environment defined')
        elif (env is staging and production is None):
            raise MalformedMoYaml('No staging heroku environment defined')
        elif (env == 'staging'):
            app = staging
        else:
            app = production

        call(["heroku", "logs", "--tail", "--app", app])

    except IOError:
        sys.exit('Cannot open mo.yml')
    except MalformedMoYaml:
        sys.exit('Malformed mo.yml file')
    except UnknownEnvironment:
        sys.exit("Unknown environment {0}".format(env))
