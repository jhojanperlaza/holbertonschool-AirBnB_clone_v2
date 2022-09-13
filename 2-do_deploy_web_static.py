#!/usr/bin/python3
"""
distributes an archive to your web servers
"""
from fabric.api import put, run
from fabric.api import env
import sys

env.hosts = ['3.91.46.188', '34.207.144.236']
env.user = sys.argv[7]


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
