from pip.req import parse_requirements
from setuptools import setup, find_packages

from helga_urbandictionary import __version__ as version

requirements = [
    str(req.req) for req in parse_requirements('requirements.txt')
]

setup(
    name='helga-urbandictionary',
    version=version,
    description=('looks up definitions for words on urban dictionary'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat :: Internet Relay Chat'],
    keywords='irc bot urbandictionary',
    author='Michael Orr',
    author_email='michael@orr.co',
    url='https://github.com/michaelorr/helga-urbandictionary',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_urbandictionary'],
    zip_safe=True,
    install_requires=requirements,
    entry_points = dict(
        helga_plugins=[
            'urbandictionary = helga_urbandictionary.plugin:urbandictionary',
        ],
    ),
)
