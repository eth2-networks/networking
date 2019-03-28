from networking.utils import get_default_backend
default_backend = get_default_backend()

get_interface = default_backend.get_interface
