Python Encapsulation describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
To prevent accidental change, an object’s variable can only be changed by an object’s method. 
    Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

Encapsulation in Python:
Class:
    -> variables
    -> methods

The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes that are hidden from the outside world.

------------------------------------------------------------------------------------
PROTECTED MEMBER 
To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.

Although the protected variable can be accessed out of the class as well as in the derived class (modified too in derived class), 
    it is customary(convention not a rule) to not access the protected out the class body.

------------------------------------------------------------------------------------
PRIVATE MEMBER 
Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. 
In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

However, to define a private member prefix the member name with double underscore “__”.

Note: Python’s private and protected members can be accessed outside the class through python name mangling. (https://www.geeksforgeeks.org/private-variables-python/)
However, the point is when we create the private member / variable we don't want & people can not access to the p-var directly, we can control the changed p-var through the @setter