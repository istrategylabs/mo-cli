import unittest
import subprocess


class InitTests(unittest.TestCase):

    def test_InitNode_fromISL(self):
        run = subprocess.run(["mo init node"], shell=True)
        self.assertEqual(run.returncode, 0)

    def test_InitFake_fromISL(self):
        run = subprocess.run("mo init fake-framework", shell=True)
        self.assertEqual(run.returncode, 1)

    def test_InitDjango_fromOtherUser(self):
        run = subprocess.run("mo init django -u sarahjaine", shell=True)
        self.assertEqual(run.returncode, 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
