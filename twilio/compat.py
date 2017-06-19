import six

# Those are not supported by the six library and needs to be done manually
try:
    # python 3
    from urllib.parse import urlencode, urlparse, urljoin, urlunparse
except ImportError:
    # python 2 backward compatibility
    # noinspection PyUnresolvedReferences
    from urllib import urlencode
    # noinspection PyUnresolvedReferences
    from urlparse import urlparse, urljoin, urlunparse

try:
    # python 2
    from itertools import izip
except ImportError:
    # python 3
    izip = zip


def string_compat(s):
    if isinstance(s, six.binary_type):
        if (six.PY2):
            # s is `str` in Python 2
            return s
        elif (six.PY3):
            # s is `bytes` in Python 3
            return s.decode('utf-8')
