
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.ai_api import AIApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from elements_sdk.api.ai_api import AIApi
from elements_sdk.api.aws_api import AWSApi
from elements_sdk.api.auth_api import AuthApi
from elements_sdk.api.automation_api import AutomationApi
from elements_sdk.api.click_api import ClickApi
from elements_sdk.api.integrations_api import IntegrationsApi
from elements_sdk.api.main_api import MainApi
from elements_sdk.api.media_library_api import MediaLibraryApi
from elements_sdk.api.private_api import PrivateApi
from elements_sdk.api.satellite_api import SatelliteApi
from elements_sdk.api.sharedstorage_api import SharedstorageApi
from elements_sdk.api.status_api import StatusApi
from elements_sdk.api.storage_api import StorageApi
from elements_sdk.api.tape_archive_api import TapeArchiveApi
