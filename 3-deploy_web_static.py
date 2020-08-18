#!/usr/bin/python3
"""Function to deploy an archive to the web servers"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['35.243.244.163', '54.146.93.68']



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


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases'
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        directory = archive.split('.')
        run("sudo mkdir -p {}/{}/".format(path, directory[0]))
        run("sudo tar -xzf /tmp/{} -C {}/{}/".format(archive,
                                                     path,
                                                     directory[0]))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo mv {}/{}/web_static/* {}/{}/".format(path, directory[0],
                                                       path, directory[0]))
        run("sudo rm -rf {}/{}/web_static".format(path, directory[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{}/ /data/web_static/current".format(path,
                                                                 directory[0]))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ script (based on the file 2-do_deploy_web_static.py) that creates
        and distributes an archive to your web servers,
        using the function deploy """
    global path

    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
