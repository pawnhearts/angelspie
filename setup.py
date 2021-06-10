#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from angelspie import __version__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="robotnaoborot",
    author_email='robotnaoborot@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="mapping global hotkeys and various actions for X11 events",
    entry_points={
        'console_scripts': [
            'angelspie=angelspie.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='angelspie',
    name='angelspie',
    packages=find_packages(include=['angelspie', 'angelspie.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pawnhearts/angelspie',
    version='0.1.5',
    zip_safe=False,
)
