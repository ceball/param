********
Advanced/background
********

internal_name

attrib_name


    # Overview of Parameters for programmers
    # ======================================
    #
    # Consider the following code:
    #
    #
    # class A(Parameterized):
    #     p = Parameter(default=1)
    #
    # a1 = A()
    # a2 = A()
    #
    #
    # * a1 and a2 share one Parameter object (A.__dict__['p']).
    #
    # * The default (class) value of p is stored in this Parameter
    #   object (A.__dict__['p'].default).
    #
    # * If the value of p is set on a1 (e.g. a1.p=2), a1's value of p
    #   is stored in a1 itself (a1.__dict__['_p_param_value'])
    #
    # * When a1.p is requested, a1.__dict__['_p_param_value'] is
    #   returned. When a2.p is requested, '_p_param_value' is not
    #   found in a2.__dict__, so A.__dict__['p'].default (i.e. A.p) is
    #   returned instead.
    #
    #
    # Be careful when referring to the 'name' of a Parameter:
    #
    # * A Parameterized class has a name for the attribute which is
    #   being represented by the Parameter ('p' in the example above);
    #   in the code, this is called the 'attrib_name'.
    #
    # * When a Parameterized instance has its own local value for a
    #   parameter, it is stored as '_X_param_value' (where X is the
    #   attrib_name for the Parameter); in the code, this is called
    #   the internal_name.


    # Because they implement __get__ and __set__, Parameters are known
    # as 'descriptors' in Python; see "Implementing Descriptors" and
    # "Invoking Descriptors" in the 'Customizing attribute access'
    # section of the Python reference manual:
    # http://docs.python.org/ref/attribute-access.html


    # Because they implement __get__ and __set__, Parameters are known
    # as 'descriptors' in Python; see "Implementing Descriptors" and
    # "Invoking Descriptors" in the 'Customizing attribute access'
    # section of the Python reference manual:
    # http://docs.python.org/ref/attribute-access.html



Creating a new parameter class
------------------------------


Note that
    # When created, a Parameter does not know which
    # Parameterized class owns it. If a Parameter subclass needs
    # to know the owning class, it can declare an 'objtype' slot
    # (which will be filled in by ParameterizedMetaclass)



Slots
_____

    # So that the extra features of Parameters do not require a lot of
    # overhead, Parameters are implemented using __slots__ (see
    # http://www.python.org/doc/2.4/ref/slots.html).  Instead of having
    # a full Python dictionary associated with each Parameter instance,
    # Parameter instances have an enumerated list (named __slots__) of
    # attributes, and reserve just enough space to store these
    # attributes.  Using __slots__ requires special support for
    # operations to copy and restore Parameters (e.g. for Python
    # persistent storage pickling); see __getstate__ and __setstate__.


    params have slots not dict so 


* 
