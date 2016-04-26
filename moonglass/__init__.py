# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
Evolved code-diff analysis.
"""

import click
import subprocess
import sys

from dulwich.errors import NotGitRepository
from dulwich.objects import ShaFile
from dulwich.repo import Repo


def _exit(msg):
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
        return "ctags command not found on the system.  Please make sure you have it installed."

    return False


def _check_repo(path):
    try:
        repo = Repo.discover(path)
    except NotGitRepository:
        return None, "No Git repository could be found using the specified path. (path: {0})".format(path)

    return repo, False


@click.command()
@click.option('--path', '-p', default='.',
              help='Location of the Git repository to scan.')
def main(path):
    """
    Evolved code-diff analysis.
    """

    err = _check_ctags()
    if err:
        _exit(err)

    repo, err = _check_repo(path)
    if err:
        _exit(err)

    for x in repo.get_walker():
        for typ, old, new in x.changes():
            if typ != 'modify':
                continue

            # TODO: compute tags for each commit, store them, then diff them.
            repo.get_object(old.sha).as_raw_string()
            repo.get_object(new.sha).as_raw_string()


if __name__ == '__main__':
    main()
