"""
All parameters should have default of None.

python -m unittest tests.testdefaultvalues
"""

import unittest

import param

from .util import make_method, param_type_test_reg


# checking default value is None


class DefaultIsNone(object):

    def __init__(self,paramtype):
        self.paramtype = paramtype

    def __call__(self,self2):

        class Tmp(param.Parameterized):
            tmp = self.paramtype()

        self2.assertEqual(Tmp.tmp,None)


### create test class and add methods

class TestDefault(unittest.TestCase):
    pass

for paramtype in param_type_test_reg:
    name = "test_%s_%s"%(DefaultIsNone.__name__, paramtype.__name__)
    make_method(DefaultIsNone(paramtype),TestDefault,method_name=name)


if __name__ == "__main__":
    import nose
    nose.runmodule()
