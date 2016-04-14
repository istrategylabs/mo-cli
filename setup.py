from setuptools import setup

setup(
        name='mo-cli',
        version='1.0',
        description='starts new "mo" cookiecutter template',
        long_description='',
        url='https://github.com/SarahJaine/mo-cli',
        author='Sarah Jaine Szekeresh',
        author_email='sarahjaine.sz@gmail.com',
        liscense='',
        classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.5',
        ],
        py_modules=['init'],
        install_requires=[
            'Click',
            'requests',
         ],
        entry_points='''
            [console_scripts]
            init=init:cli
        '''
)
