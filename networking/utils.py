import platform

from networking.backend.ioctl import IoctlBackend
from networking.backend.ioctl.platform import freebsd
from networking.backend.netlink import NetlinkBackend


def get_default_backend():
    system = platform.system()

    if system in ('Linux',):
        return NetlinkBackend()

    if system in ('FreeBSD',):
        return IoctlBackend(freebsd)

    raise EnvironmentError('Unknown platform "{}"'.format(system))
