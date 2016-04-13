import click
import subprocess

@click.command()
@click.argument('framework', type=str)
def cli(framework):
    """Starts cookiecuttter for new 'mo' project.
    Type init 'some-framework' to get started."""
    # format framework name into url string
    framework = framework.lower().replace(' ', '-')
    git_url = "https://github.com/istrategylabs/mo-"+framework
    response = subprocess.check_output(
        'curl -Is {0} | head -n 1'.format(git_url),
        shell=True)
    # convert response to string, native format is bytes
    if "HTTP/1.1 200 OK" in str(response):
        click.echo(response)
    else:
        click.echo("No 'mo' project found for '{0}'.\n"
                   "Check https://github.com/istrategylabs "
                   "for available 'mo' projects."
                   .format(framework))
