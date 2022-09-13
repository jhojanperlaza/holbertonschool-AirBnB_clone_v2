#!/usr/bin/python3
"""
script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
import time


def do_pack():
    local("mkdir -p versions")
    get_time = time.localtime()  # get struct_time
    time_string = time.strftime("web_static_%Y%m%d%H%M%S", get_time)

    command = local("tar -cvzf versions/{}.tgz web_static".format(time_string))

    if command.failed:
        return None
