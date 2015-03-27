"""
Test cases for param inheritance mecahnism.

python -m unittest tests.testinheritance
"""

import unittest

import param

from .util import make_method, param_type_test_reg

    
class A(param.Parameterized):
    a = param.Parameter("something unique")
    b = param.Parameter(None)
    c = param.Parameter("4th")


class _setup(object):

    def __init__(self,paramtype,value):
        self.paramtype = paramtype
        self.value = value

        class B(A):
            a = self.paramtype(self.value)
            b = self.paramtype()
            c = self.paramtype()

        self.B = B

                
class OverrideInheritance(_setup):
    """
    B.a should be set to the specified value rather than inheriting from A.
    """
    def __call__(self,self2):
        self2.assertEqual(self.B.a, self.value)


class InheritDefault(_setup):
    """
    B.b and B.c should inherit A's values
    """
    def __call__(self,self2):
        self2.assertEqual(self.B.b, A.b) 
        self2.assertEqual(self.B.c, A.c)


#class Unset(_setup):
#    def __call__(self,self2):
#        self2.assertEqual(self.B.b,None) # will be unset
#        self2.assertEqual(self.B().b,None) # will be unset


        
testing = [OverrideInheritance,
           #Unset,
           InheritDefault]


### create TestCase class & add methods

class TestInheritance(unittest.TestCase):
    pass
    
for paramtype,values in param_type_test_reg.items():
    for value in values:
        for cl in testing:
            name = "test_%s_%s%s"%(cl.__name__,paramtype.__name__,value)
            make_method(cl(paramtype,value),TestInheritance,method_name=name)

if __name__ == "__main__":
    import nose
    nose.runmodule()
