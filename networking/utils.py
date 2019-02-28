import platform

from networking.backend.ioctl import IoctlBackend
from networking.backend.netlink import NetlinkBackend


def get_default_backend():
    system = platform.system()

    if system in ('Linux',):
        return NetlinkBackend

    if system in ('FreeBSD', 'NetBSD',):
        return IoctlBackend

    raise EnvironmentError('Unknown platform "{}"'.format(system))
