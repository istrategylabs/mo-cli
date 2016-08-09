import click
import sys
from functools import update_wrapper
from errors import UnknownEnvironment
from helpers import find_config, determine_toolbelt_status


class supported_envs(object):

    def __init__(self, *argv):
        self.envs = argv

    def __call__(self, f):
        """Checks to ensure that the correct environment is being specified
        in the context of the current command. It assumes the precence of the
        require_config decorator
        """
        @click.pass_context
        def wrapped_f(ctx, *args, **kwargs):
            env = kwargs.get('env')
            try:
                # Supported environments are staging and production
                if env not in self.envs:
                    err = "Environment '{0}' is not supported!".format(env)
                    raise UnknownEnvironment(err)

            except UnknownEnvironment as err:
                sys.exit(err)

            return ctx.invoke(f, *args, **kwargs)
        return update_wrapper(wrapped_f, f)


def require_config(func):
    """This decorator ensures that the mo configuration is loaded and
    available
    """
    data = find_config()

    if data is None:
        data = {}

    @click.pass_context
    def wrapper(ctx, *args, **kwargs):
        return ctx.invoke(func, *args, config=data, **kwargs)

    return update_wrapper(wrapper, func)


def require_heroku_toolbelt(func):
    """This decorator determines whether or not the heroku toolbelt
    is installed. It's required for certain mo commands
    """

    install_url = "https://toolbelt.heroku.com/"
    install_err = "You must install the heroku toolbelt. Get it at {0}"\
        .format(install_url)

    code = determine_toolbelt_status()

    if code != 0:
        sys.exit(install_err)

    @click.pass_context
    def wrapper(ctx, *args, **kwargs):
        return ctx.invoke(func, *args, **kwargs)

    return update_wrapper(wrapper, func)
