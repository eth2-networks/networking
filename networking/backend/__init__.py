class BaseBackend(object):
    def get_interface(self, name):
        raise NotImplementedError
