# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
Setup file for moonglass.
"""

from setuptools import setup

setup(name='moonglass',
      version='0.0.1',
      author='Bheesham Persaud',
      license='GPLv2',
      url='https://github.com/bheesham/moonglass',
      description='Evolved code-diff analysis.',
      packages=['moonglass'],
      install_requires=[
          'click',
          'dulwich'
      ],
      entry_points={
          'console_scripts': [
              'mg=moonglass:main'
          ]
      })
