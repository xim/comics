from settings_dev import *

# Remove cache middleware when running tests, as these cause problems in
# django.contrib.{admin,auth,session} unit tests.
MIDDLEWARE_CLASSES = [i for i in MIDDLEWARE_CLASSES
    if not i.startswith('django.middleware.cache')]
