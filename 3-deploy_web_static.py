#!/usr/bin/python3
"""
script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
from fabric.api import put, run
from fabric.api import env
import time

env.hosts = ['3.91.46.188', '34.207.144.236']
env.user = 'ubuntu'
env.key_ssh = '~/.ssh/school'


def do_pack():
    """ generates a .tgz archive """
    local("mkdir -p versions")
    get_time = time.localtime()  # get struct_time
    time_string = time.strftime("web_static_%Y%m%d%H%M%S", get_time)

    command = "versions/{}.tgz".format(time_string)
    command_exc = local("tar -cvzf {} web_static".format(command))

    if command_exc.failed:
        return None
    else:
        return command


def do_deploy(archive_path):
    """ distributes an archive"""
    if not archive_path:
        return False
    filename_tgz = archive_path.split('/')[1]
    filename = filename_tgz.split('.')[0]

    string_path = "/data/web_static/releases/{}/".format(filename)

    try:
        put(archive_path, '/tmp/{}'.format(filename_tgz))
        run("mkdir -p {}".format(string_path))
        run("tar -xzf /tmp/{} -C {}".format(filename_tgz, string_path))
        run("rm /tmp/{}".format(filename_tgz))
        run("mv {}web_static/* {}".format(string_path, string_path))
        run("rm -rf {}web_static".format(string_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(string_path))
        return True
    except Exception:
        return False


def deploy():
    """deploy functionality"""
    path = do_pack()
    if not path:
        return False

    return do_deploy(path)
