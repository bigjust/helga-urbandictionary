import os
from setuptools import setup, find_packages

from helga_urbandictionary import __version__ as version

requirements = []
with open(
    os.path.join(
        os.path.dirname(__file__),
        'requirements.txt',
    ),
    'r'
) as in_:
    requirements = in_.readlines()


setup(
    name="helga-urbandictionary",
    version=version,
    description=('looks up definitions for words on urban dictionary'),
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: IRC',
        'Intended Audience :: Twisted Developers, IRC Bot Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: IRC Bots'],
    keywords='irc bot urbandictionary',
    author='Michael Orr',
    author_email='michael@orr.co',
    url='https://github.com/michaelorr/helga-urbandictionary',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga-urbandictionary'],
    zip_safe=True,
    install_requirements=requirements,
    entry_points = dict(
        helga_plugins=[
            'urbandictionary = helga_urbandictionary.plugin:urbandictionary',
        ],
    ),
)
