"""
Stuff
"""

import new

import param

# CEBALERT: move elsewhere/not yet all/discover them instead
param_type_test_reg = {
    # param type : some values to test with
    param.Parameter: (None, "something"),
    param.String: (None, "test", ""),
    param.Number: (None, 1.0),
    param.Boolean: (None, False),
#    param.Integer: (None, 1),
    param.Magnitude: (None, 1.0),
#    param.Tuple: (None, (1,)),
#    param.NumericTuple: (None, (1,)),
    param.Callable: (None, lambda:1 ),
    param.ObjectSelector: (None, 1),
#    param.List: (None, [1]),
#    param.Dict: (None, {1:1}),
}


def make_method(func,clas,method_name):
    method = new.instancemethod(func,None,clas)
    setattr(clas,method_name,method)
    #if not method_name: method_name=func.__name__
    #clas.__dict__[method_name]=method

