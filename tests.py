from mo import init
from click.testing import CliRunner


runner = CliRunner()
test_initDjango_fromIsl = runner.invoke(init, ['django'])
assert test_initDjango_fromIsl.exit_code == 0

test_initDjango_fromUser = runner.invoke(init, ['django', '-u', 'sarahjaine'])
assert test_initDjango_fromUser.exit_code == 0

test_initFake_fromIsl = runner.invoke(init, ['fake'])
assert test_initFake_fromIsl.exit_code != 0
