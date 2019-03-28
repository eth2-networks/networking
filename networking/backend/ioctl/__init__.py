import socket

from networking.backend import BaseBackend
from networking.backend.ioctl.interfaces import IoctlInterface


class IoctlBackend(BaseBackend):
    def __init__(self, platform):
        self.platform = platform

    def get_interface(self, name):
        return IoctlInterface(name, self)
