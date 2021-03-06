try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

from os.path import join, dirname

import mock

# Example config
CONFIG_EXAMPLE = join(dirname(dirname(dirname(__file__))), 'redsample.config.example')

def json_response(json_):
    return mock.Mock(return_value=json_)
