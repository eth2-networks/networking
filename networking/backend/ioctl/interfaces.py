from networking.interfaces import Interface


class IoctlInterface(Interface):
    def __init__(self, name, backend):
        self.name = name
        self._backend = backend

    def _get_mtu(self):
        print(self._backend.platform.SIOCGIFMTU)
        raise NotImplementedError

    def _set_mtu(self, mtu):
        raise NotImplementedError
