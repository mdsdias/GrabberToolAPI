import os
from setuptools import setup

from distutils.core import Command


class Tests(Command):
    description = "Testes de run"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import unittest

        runner = unittest.runner.TextTestRunner()
        test_loader = unittest.TestLoader()
        test = test_loader.discover("tests")
        runner.run(test)


setup(
    name='grabbertool',
    version='1.0.0',
    author="Isqneeh",
    author_email="isqneimortal@gmail.com",
    keywords="api puxar dados grabbertool",
    packages=['grabbertool'],
    url='https://github.com/isqneeh/GrabberToolAPI',
    description='GrabberTool, A ferramenta para puxar dados agora ficou mais facil',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires='requests>=2.4.3',
    cmdclass = {'test': Tests},
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developer",
        "Operating System :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python 2.7",
        "Programming Language :: Python 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: Freely Distributable",
    ],
)