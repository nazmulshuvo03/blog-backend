from .base import *  # noqa: F401


DEBUG = False
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ORIGIN_ALLOW_ALL = True
