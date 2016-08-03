import click
from functools import update_wrapper
from errors import UnknownEnvironment


class supported_envs(object):

    def __init__(self, *argv):
        self.envs = argv

    def __call__(self, f):
        @click.pass_context
        def wrapped_f(ctx, *args, **kwargs):
            env = kwargs.get('env')
            # Supported environments are staging and production
            if (env != 'staging' and env != 'production'):
                raise UnknownEnvironment("Unknown environment {0}".format(env))
            return ctx.invoke(f, *args, **kwargs)
        return update_wrapper(wrapped_f, f)
