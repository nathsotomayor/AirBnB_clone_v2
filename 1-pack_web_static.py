#!/usr/bin/python3
"""Function that creates package .tgz from 'web_static'
folder of AirBnB Clone repo"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create .tgz archive"""
    get_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(get_time)
    if file_name is not None:
        local("mkdir -p ./versions")
        local("tar -cvzf {} ./web_static".format(file_name))
        return file_name
    else:
        return None
