class Interface(object):
    def _get_mtu(self):
        raise NotImplementedError

    def _set_mtu(self, mtu):
        raise NotImplementedError

    mtu = property(fget=lambda self: self._get_mtu(),
                   fset=lambda self, mtu: self._set_mtu(mtu))
