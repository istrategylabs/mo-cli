from setuptools import setup

setup(
        name='mo-cli',
        version='1.0',
        py_modules=['init'],
        install_requires=[
            'Click',
         ],
        entry_points='''
            [console_scripts]
            init=init:cli
        '''
)
