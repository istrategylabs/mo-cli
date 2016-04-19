from setuptools import setup

long_description = open('README.md').read()

setup(
        name='mo-cli',
        version='0.1',
        description='CLI for mo cookiecutter projects',
        long_description=long_description,
        url='https://github.com/istrategylabs/mo-cli',
        author='Sarah-Jaine Szekeresh',
        author_email='sarahjaine@isl.co',
        liscense='MIT',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.5',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        py_modules=['mo'],
        install_requires=[
            'click>=6.6,<7',
            'cookiecutter>=1.4,<2',
            'requests>=2.9.1,<3',
         ],
        entry_points='''
            [console_scripts]
            mo=mo:cli
        '''
)
