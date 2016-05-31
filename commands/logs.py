
from errors import MalformedMoYaml
from errors import UnknownEnvironment
from subprocess import call
import click
import yaml
import io


def command_logs(env):
    click.echo(env)
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
        if (env is not 'staging' and env is not 'production'):
            raise UnknownEnvironment("Unknown environment {0}".format(env))

        # If the specified (or default) environment is not configured, raise
        # an error
        if (env is 'production' and production is None):
            raise MalformedMoYaml('No production heroku environment defined')
        elif (env is staging and production is None):
            raise MalformedMoYaml('No staging heroku environment defined')
        elif (env is production):
            app = staging
        else:
            app = production

        call(["heroku", "logs", "--tail", "--app", app])

    except IOError:
        click.echo('Cannot open mo.yml')
    except MalformedMoYaml:
        click.echo('Malformed mo.yml file')
