from cookiecutter.main import cookiecutter
from errors import MalformedMoYaml
from subprocess import call
import click
import requests
import yaml
import sys
import io


def cookie_find(url):
    try:
        response = requests.head(url)
        if response.status_code != 200:
            sys.exit("{0} not found.".format(url))
        else:
            return response.status_code
    except requests.exceptions.ConnectionError as e:
        sys.exit("Encountered an error with the connection.")
    except Exception as e:
        sys.exit(e)


@click.group()
def cli():
    '''Command-line utility to work with cookiecutter templates from GitHub repos.
    Search https://github.com/istrategylabs 'mo' projects
    to see available ISL cookiecutters.'''
    pass


@cli.command()
@click.argument('framework', type=click.STRING)
@click.option('--user', '-u',
              help='Specify git account to use for cookiecutters',
              default='istrategylabs')
def init(framework, user):
    '''initialize a new cookiecutter template'''

    # Check that cookiecutter template exists for requested framework
    git_url = 'https://github.com/'
    framework = framework.lower().replace(' ', '-')
    mo_url = "{0}{1}/mo-{2}".format(git_url, user, framework)
    cookie_find(mo_url)

    # Run cookiecutter template
    if click.confirm('Ready to start cookiecutter {0}.git '
                     'in the current directory.\n'
                     'Do you want to continue?'.format(mo_url)):
        try:
            cookiecutter('{0}.git'.format(mo_url))
        except:
            sys.exit("Problem encounted while cloning '{0}.git'"
                     .format(mo_url))


@cli.command()
@click.option('--env', '-e',
			  help='Tail logs for the current mo app',
			  default='production')
def logs(env):
	try:
		stream = io.open('mo.yml', 'r')
		data = yaml.load(stream)
		heroku_envs = data.get('heroku')
		if (heroku_envs is None):
			raise MalformedMoYaml('No heroku apps defined for this project')
		staging = heroku_envs.get('staging')
		production = heroku_envs.get('production')

		if (env is 'production' and production is None):
			raise MalformedMoYaml('No production heroku environment defined')
		elif (env is staging and production is None):
			raise MalformedMoYaml('No staging heroku environment defined')
		else:
			call(["heroku", "logs", "--tail", "--app", env])
	except IOError:
		click.echo('Cannot open mo.yaml')

if __name__ == '__main__':
    logs()
