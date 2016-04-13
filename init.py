import click
import subprocess
import requests


@click.command()
@click.argument('framework', type=str)
def cli(framework):
    """Starts new 'mo' project.
    Type init 'some-framework' to get started."""
    # Format framework name into url string
    framework = framework.lower().replace(' ', '-')
    git_url = "https://github.com/istrategylabs/mo-"+framework
    response = requests.get(git_url)
    status = response.status_code
    if status == 200:
        # Check for homebrew, install if missing
        homebrew_check = subprocess.run("which -s brew", shell=True)
        if homebrew_check.returncode == 1:
            subprocess.run('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"',
                           shell=True)
        # Check for cookiecutter, install if missing
        brew_list = subprocess.check_output('brew list', shell=True)
        if "cookiecutter" not in str(brew_list):
            subprocess.run('brew install cookiecutter', shell=True)
        # Start cookiecuter process for framework
        subprocess.run('cookiecutter gh:istrategylabs/mo-{0}'
                       .format(framework), shell=True)
    else:
        click.echo("No 'mo' project found for '{0}'.\n"
                   "Check https://github.com/istrategylabs "
                   "for available 'mo' projects."
                   .format(framework))
