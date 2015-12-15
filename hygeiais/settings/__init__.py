import platform
from .global_settings import *

# development platforms
dev_platforms = "dr",

# production platforms
prod_platforms = ()

# get current node
current_node = platform.node()

if current_node in prod_platforms:
    from .prod_settings import *
else:
    """ Mix in settings depends on platform. """
    from .dev_settings import *
