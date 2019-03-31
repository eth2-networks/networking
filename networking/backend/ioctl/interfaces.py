import socket
import struct
from fcntl import ioctl

from networking.interfaces import Interface


class IoctlInterface(Interface):
    def __init__(self, name, backend):
        self.name = name
        self._backend = backend

        # ioctl socket
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    def _ioctl(self, ioctl, data=None, bufsize=None):
        if data and bufsize:
            raise RuntimeError('Cannot specify both data and buffer size')

        # Build ifreq struct
        ifr = bytes(name.encode('utf8'))
        ifr += b'\0' * (self._backend.platform.IFNAMESIZ - len(ifr))

        hlen = len(ifr)

        if data:
            ifr += data

        if bufsize:
            ifr += b'\0' * bufsize

        res = ioctl(self._socket, ioctl, ifr)

        return res[hlen:]

    def _get_mtu(self):
        res = self._ioctl(self._backend.platform.SIOCGIFMTU, bufsize=4)
        mtu, = struct.unpack('@i', res)

        return mtu

    def _set_mtu(self, mtu):
        ifr = self.__ifr + struct.pack('@i', mtu)
        ioctl(self._socket, self._backend.platform.SIOCSIFMTU, ifr)
