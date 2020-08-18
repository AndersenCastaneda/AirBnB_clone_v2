#!/usr/bin/python3
"""Generates a .tgz archive from web_static content folder"""

from fabric.operations import local, run, put, env
from datetime import datetime
from os import path

# servers ip
env.hosts = ["35.231.98.181", "35.237.106.108"]
# user for the servers
env.user = "ubuntu"


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """Distributes an archive to your servers"""
    if not path.exists(archive_path):
        return False

    # Upload the file to /tmp directory on the web server
    put(archive_path, "/tmp/")

    # Get directory name from arvhice (removing extension)
    arch = archive_path.split("/")[1].replace(".tgz", "")

    # Path for the archive
    archiveDir = "/data/web_static/releases/" + arch

    # Create directory path
    run("mkdir -p {}".format(archiveDir))

    # Get archive name from archive path
    archive = archive_path.split("/")[1]

    # Decompress archive in the path
    # -x: Extract files from an archive
    # -z: Uncompress whit gzip command
    # -f: use archive file or device ARCHIVE
    # -C: Change to directory.
    run("tar -xzf /tmp/{} -C {}".format(archive, archiveDir))

    # Delete the archive from the web server
    run("rm /tmp/{}.tgz".format(archive))

    # Delete the symbolic link /data/web_static/current from the server
    run("rm -rf /data/web_static/current")

    # Create a new the symbolic link
    run("ln -s {} /data/web_static/current".format(archiveDir))
    return True
