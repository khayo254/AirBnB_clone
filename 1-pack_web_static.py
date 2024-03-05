#!/usr/bin/python3
"""
Fabric script to generate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_{{ date }}'.format(time.strftime("%Y%m%d%H%M%S")) + '.tgz'
    local('mkdir -p versions')
    run('tar -cvzf versions/{} web_static'.format(archive))
    if run().failed:
        return None
    else:
        put(archive, 'versions/')
        return archive
