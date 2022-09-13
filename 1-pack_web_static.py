#!/usr/bin/python3
"""
script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
import time


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
