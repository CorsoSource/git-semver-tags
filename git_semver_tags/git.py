import subprocess
from subprocess import Popen, PIPE


from .version import Version


def highest_tagged_git_version(repo_location):
    """Ask the git repo what the most recent tagged commit on the index is."""

    with subprocess.Popen(
            ['git', 'describe', '--tags', '--match', 'v[[:digit:]]*', 'HEAD'],
            stdin=PIPE, stdout=PIPE, stderr=PIPE,
            cwd=os.path.abspath('../'),
        ) as cli_cmd:

        stdout, stderr = cli_cmd.communicate()

        tag = str(stdout.splitlines()[0], encoding='utf-8')
    
    version = Version(tag)

    return version



