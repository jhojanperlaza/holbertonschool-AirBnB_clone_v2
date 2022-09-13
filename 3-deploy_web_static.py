#!/usr/bin/python3
"""
Creates and distributes an archive
to your web servers
"""
from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['3.91.46.188', '34.207.144.236']
env.user = 'ubuntu'
env.key_ssh = '~/.ssh/school'


def deploy():
    path = do_pack()
    if not path:
        return False
    new_deploy = do_deploy(path)
    return new_deploy
