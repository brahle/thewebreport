# Shared settings

from thewebreport.settings_global import *

try:
    from thewebreport.settings_local import *
except ImportError:
    print('Failed to load local settings! Make sure settings_local file is present.')
    exit(1)


