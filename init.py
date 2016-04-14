import click
import requests
import subprocess
import sys


# Note: add verbose mode to see more error code
@click.command()
@click.argument("framework", type=str)
def cli(framework):
    """Command-line utility to start projects from ISL cookiecutters.
    Search https://github.com/istrategylabs repositories for 'mo' projects
    to see available ISL cookiecutters.\n
    Type init "some-framework" to get started."""
    # Check that ISL cookiecutter exists
    isl_url = "https://github.com/istrategylabs"
    framework = framework.lower().replace(" ", "-")
    mo_url = isl_url+"/mo-"+framework
    response = requests.head(mo_url)
    status = response.status_code
    # Note: add permisiion error, and some other commmon errors
    if status != 200:
        click.echo("No 'mo' project found for '{0}'.\n"
                   "Check {1} for 'mo' projects.".format(isl_url, framework))
    else:
        # Check for cookiecutter, ask sto resolve if missing
        cookie_check = subprocess.call("which -s cookiecutter", shell=True)
        if cookie_check != 0:
            brew_check = subprocess.call("which -s brew", shell=True)
            if brew_check != 0:
                click.echo("Mo-cli needs cookiecutter utility to continue. "
                           "Check out https://github.com/audreyr/cookiecutter "
                           "for installation instructions.")
                sys.exit()
            else:
                if click.confirm("Mo-cli needs cookiecutter utility to "
                                 "continue. "
                                 "Allow brew install of cookiecutter:",
                                 abort=True):
                    subprocess.call("brew install cookiecutter", shell=True)
        # Check for user confirmation before cookiecutter
        if click.confirm("Ready to start cookiecutter gh:istrategylabs/mo-{0} "
                         "in the current directory.\n"
                         "Do you want to continue?".format(framework)):
            subprocess.call("cookiecutter gh:istrategylabs/mo-{0}"
                            .format(framework), shell=True)
