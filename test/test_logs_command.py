from mo import logs
from click.testing import CliRunner
from os.path import join, dirname
from dotenv import load_dotenv
import yaml
import os
import unittest

env = os.getenv('ENVIRONMENT')

if (env == 'development'):
    dotenv_path = join(dirname(__file__), '../test.env')
    load_dotenv(dotenv_path)


class LogsTests(unittest.TestCase):

    def test_it(self, **kwargs):
        app = os.environ.get('HEROKU_TEST_APP')
        runner = CliRunner()
        data = {
            'domain': 'my-app.com',
            'heroku': {
                'staging': "{0}-staging".format(app),
                'production': app
            }
        }
        mo_yml_path = join(dirname(__file__), 'mo.yml')

        with open(mo_yml_path, 'w') as mo_yml:
            mo_yml.write(yaml.dump(data, default_flow_style=False))
            # TODO: Need to terminate logging output OR mock it
            # test_logs = runner.invoke(logs)
            # assert test_logs.exit_code == 0
            os.remove(mo_yml_path)
