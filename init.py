import click
import requests
import subprocess
import sys


@click.command()
@click.argument('framework', type=click.STRING)
@click.option('--user', '-u',
              help='Specify git account to use for cookiecutters',
              default='istrategylabs')
def cli(framework, user):
    '''Command-line utility to start cookiecutter templates from GitHub repos.
    Search https://github.com/istrategylabs 'mo' projects
    to see available ISL cookiecutters.\n
    Type init 'some-framework' to get started.'''

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

    # Check for cookiecutter tool, install if missing
    cookie_check = subprocess.call('which -s cookiecutter', shell=True)
    if cookie_check != 0:
        brew_check = subprocess.call('which -s brew', shell=True)
        # Exit users if they don't have cookiecutter or homebrew
        if brew_check != 0:
            sys.exit('Mo-cli needs cookiecutter utility to continue. '
                     'Check out https://github.com/audreyr/cookiecutter '
                     'for installation instructions.')
        if click.confirm('Mo-cli needs cookiecutter utility to continue. '
                         'Allow brew install of cookiecutter?',
                         abort=True):
            subprocess.call('brew install cookiecutter', shell=True)

    # Run cookiecutter template
    if click.confirm('Ready to start cookiecutter gh:{0}/mo-{1} '
                     'in the current directory.\n'
                     'Do you want to continue?'.format(user, framework)):
        try:
            subprocess.check_call('cookiecutter gh:{0}/mo-{1}'
                                  .format(user, framework), shell=True,
                                  stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            sys.exit("Problem encounted while cloning '{0}'.".format(mo_url))
