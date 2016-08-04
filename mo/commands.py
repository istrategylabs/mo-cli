
from subprocess import call
from mo.errors import MalformedMoYaml
import click
import sys


def logs(env, **kwargs):
    """Executes the heroku logs command with the tail flag. The default
    environment is staging but production can be tailed using the environment
    flag
    """
    config = kwargs.get('config')
    envs = config.get('heroku')
    app = envs.get(env)

    try:
        # If there is no heroku section of the mo.yml file,
        # raise an error
        if (envs is None):
            err = 'No heroku apps defined for this project'
            raise MalformedMoYaml(err)

        configured_env = envs.get(env)

        if (configured_env is None):
            err = 'No {0} heroku environment defined'.format(env)
            raise MalformedMoYaml(err)

    except MalformedMoYaml as err:
        sys.exit(err)

    click.echo("\n   heroku logs --tail --app {0}\n".format(app))
    call(["heroku", "logs", "--tail", "--app", app])
