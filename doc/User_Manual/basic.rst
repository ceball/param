*****
Basic
*****



    Parameters are a special kind of class attribute.  Setting a
    Parameterized class attribute to be a Parameter instance causes
    that attribute of the class (and the class's instances) to be
    treated as a Parameter.  This allows special behavior, including
    dynamically generated parameter values, documentation strings,
    constant and read-only parameters, and type or range checking at
    assignment time.

    For example, suppose someone wants to define two new kinds of
    objects Foo and Bar, such that Bar has a parameter delta, Foo is a
    subclass of Bar, and Foo has parameters alpha, sigma, and gamma
    (and delta inherited from Bar).  She would begin her class
    definitions with something like this:

    class Bar(Parameterized):
        delta = Parameter(default=0.6, doc='The difference between steps.')
        ...

    class Foo(Bar):
        alpha = Parameter(default=0.1, doc='The starting value.')
        sigma = Parameter(default=0.5, doc='The standard deviation.',
                          constant=True)
        gamma = Parameter(default=1.0, doc='The ending value.')
        ...

    Class Foo would then have four parameters, with delta defaulting
    to 0.6.

    Parameters have several advantages over plain attributes:

    1. Parameters can be set automatically when an instance is
       constructed: The default constructor for Foo (and Bar) will
       accept arbitrary keyword arguments, each of which can be used
       to specify the value of a Parameter of Foo (or any of Foo's
       superclasses).  E.g., if a script does this:

           myfoo = Foo(alpha=0.5)

       myfoo.alpha will return 0.5, without the Foo constructor
       needing special code to set alpha.

       If Foo implements its own constructor, keyword arguments will
       still be accepted if the constructor accepts a dictionary of
       keyword arguments (as in ``def __init__(self,**params):``), and
       then each class calls its superclass (as in
       ``super(Foo,self).__init__(**params)``) so that the
       Parameterized constructor will process the keywords.

    2. A Parameterized class need specify only the attributes of a
       Parameter whose values differ from those declared in
       superclasses; the other values will be inherited.  E.g. if Foo
       declares

        delta = Parameter(default=0.2)

       the default value of 0.2 will override the 0.6 inherited from
       Bar, but the doc will be inherited from Bar.

    3. The Parameter descriptor class can be subclassed to provide
       more complex behavior, allowing special types of parameters
       that, for example, require their values to be numbers in
       certain ranges, generate their values dynamically from a random
       distribution, or read their values from a file or other
       external source.

    4. The attributes associated with Parameters provide enough
       information for automatically generating property sheets in
       graphical user interfaces, allowing Parameterized instances to
       be edited by users.

    Note that Parameters can only be used when set as class attributes
    of Parameterized classes. Parameters used as standalone objects,
    or as class attributes of non-Parameterized classes, will not have
    the behavior described here.









    Automatic object naming: Every Parameterized instance has a name
    parameter.  If the user doesn't designate a name=<str> argument
    when constructing the object, the object will be given a name
    consisting of its class name followed by a unique 5-digit number.

    Automatic parameter setting: The Parameterized __init__ method
    will automatically read the list of keyword parameters.  If any
    keyword matches the name of a Parameter (see Parameter class)
    defined in the object's class or any of its superclasses, that
    parameter in the instance will get the value given as a keyword
    argument.  For example:

      class Foo(Parameterized):
         xx = Parameter(default=1)

      foo = Foo(xx=20)

    in this case foo.xx gets the value 20.

    When initializing a Parameterized instance ('foo' in the example
    above), the values of parameters can be supplied as keyword
    arguments to the constructor (using parametername=parametervalue);
    these values will override the class default values for this one
    instance.

    If no 'name' parameter is supplied, self.name defaults to the
    object's class name with a unique number appended to it.

    Message formatting: Each Parameterized instance has several
    methods for optionally printing output. This functionality is
    based on the standard Python 'logging' module; using the methods
    provided here, wraps calls to the 'logging' module's root logger
    and prepends each message with information about the instance
    from which the call was made. For more information on how to set
    the global logging level and change the default message prefix,
    see documentation for the 'logging' module.







warning when you set non-parameter on PO


__abstract


precedence


allow_None


instantiate



constant
        If the Parameter's constant attribute is True, only allows
        the value to be set for a Parameterized class or on
        uninitialized Parameterized instances.

readonly

        If the Parameter's readonly attribute is True, only allows the
        value to be specified in the Parameter declaration inside the
        Parameterized source code. A read-only parameter also
        cannot be set on a Parameterized class.

        Note that until we support some form of read-only
        object, it is still possible to change the attributes of the
        object stored in a constant or read-only Parameter (e.g. the
        left bound of a BoundingBox).




Time
----



Logging
-------
