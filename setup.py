from setuptools import setup

setup(
        name='mo-cli',
        version='0.1.0',
        description='starts new "mo" cookiecutter template',
        long_description='',
        url='https://github.com/SarahJaine/mo-cli',
        author='Sarah Jaine Szekeresh',
        author_email='sarahjaine@isl.co',
        liscense='MIT',
        classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3.5',
        ],
        py_modules=['init'],
        install_requires=[
            'click',
            'requests',
            'cookiecutter,'
         ],
        entry_points='''
            [console_scripts]
            init=init:cli
        '''
)
