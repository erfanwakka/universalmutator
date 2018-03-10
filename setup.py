#-*- coding:utf-8 -*-

from setuptools import setup, find_packages
import sys, os

setup(
    name='universalmutator',
    version='0.8.4',
    description='Universal regexp-based mutation tool',
    long_description=open('README.md').read(),
    packages=['universalmutator',],
    include_package_data = True,
    package_data = {
        'universalmutator': [
            'static/universal.rules',
            'static/c_like.rules',
            'static/c.rules',
            'static/cpp.rules',
            'static/swift.rules',
            'static/java.rules',
            'static/python.rules',
            'static/none.rules',
            'static/handlemutant.py'            
            ]
    },
    license='MIT',
    entry_points="""
    [console_scripts]
    mutate = universalmutator.genmutants:main
    analyze_mutants = universalmutator.analyze:main
    check_covered = universalmutator.checkcov:main
    """,
    keywords='testing mutation mutation-testing',
    classifiers=[
      "Intended Audience :: Developers",
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 2",
      ],
    install_requires=[
    ],
    url='https://github.com/agroce/universalmutator',
)
