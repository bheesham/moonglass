# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
Evolved code-diff analysis.
"""

import click
import subprocess
import sys

from dulwich.errors import NotGitRepository
from dulwich.diff_tree import walk_trees
from dulwich.repo import Repo


def _error(msg):
    sys.stderr.write(msg + '\n')
    sys.exit(1)


def _check_ctags():
    """
    Makes sure ctags, the heart of this project, is installed before running.
    """

    try:
        subprocess.check_call(['which', 'ctags'],
                              stdin=subprocess.DEVNULL,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)

    except subprocess.CalledProcessError:
        _error("ctags command not found on the system.  Please make sure you have it installed.")


def _check_repo(path):
    try:
        repo = Repo.discover(path)
    except NotGitRepository:
        _error("No Git repository could be found using the specified path. (path: {0})".format(path))


@click.command()
@click.option('--path', '-p', default='.',
              help='Location of the Git repository to scan.')
def main(path):
    """
    Evolved code-diff analysis.
    """

    _check_ctags()
    _check_repo(path)


if __name__ == '__main__':
    main()
