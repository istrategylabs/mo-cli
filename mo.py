from cookiecutter.main import cookiecutter
import click
import requests
import sys


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
    mo_url = git_url+user+'/mo-'+framework
    try:
        response = requests.head(mo_url)
        status = response.status_code
    except requests.exceptions.ConnectionError as e:
        sys.exit("Encountered an error with the connection.")
    except Exception as e:
        sys.exit(e)
    if status != 200:
        sys.exit("No '{0}' cookiecutter found at {1}."
                 .format(framework, git_url+user))

    # Run cookiecutter template
    if click.confirm('Ready to start cookiecutter {0}.git '
                     'in the current directory.\n'
                     'Do you want to continue?'.format(mo_url)):
        try:
            cookiecutter(mo_url+'.git')
        except:
            sys.exit("Problem encounted while cloning '{0}'.git"
                     .format(mo_url))
