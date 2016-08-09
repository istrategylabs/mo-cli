
from mo.cli import init, cookie_find
from click.testing import CliRunner
import unittest
import requests
import requests_mock

@requests_mock.Mocker(kw='mock')
class InitTests(unittest.TestCase):
    def test_cookieFind_statusCode_success(self, **kwargs):
        kwargs['mock'].head('http://test.com', status_code=200)
        self.assertEqual(cookie_find('http://test.com'),
                         requests.head('http://test.com').status_code)

    def test_cookieFind_statusCode_failure(self, **kwargs):
        kwargs['mock'].head('http://test.com/fail', status_code=404)
        with self.assertRaises(SystemExit) as cm:
            cookie_find('http://test.com/fail')
        self.assertEqual(cm.exception.code, 'http://test.com/fail not found.')


def main():
    unittest.main()

if __name__ == '__main__':
    main()

runner = CliRunner()
test_initDjango_fromIsl = runner.invoke(init, ['django'])
assert test_initDjango_fromIsl.exit_code == 0

test_initDjango_fromUser = runner.invoke(init, ['django', '-u', 'sarahjaine'])
assert test_initDjango_fromUser.exit_code == 0

test_initFake_fromIsl = runner.invoke(init, ['fake'])
assert test_initFake_fromIsl.exit_code != 0
