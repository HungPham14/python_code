Abstraction (from the Latin abs, meaning away from and trahere , meaning to draw) is the process of taking away or removing characteristics from something in order to reduce it to a set of essential characteristics.

Abstraction is that feature in OOP concept wherein the user is kept unaware of the basic implementation of a function properly. 
The user is only able to view basic functionalities whereas the internal details are hidden.

Basically, Abstraction focuses on hiding the internal implementations of a process or method from the user. 
In this way, the user knows what he is doing but not how the work is being done.

-------------------------------------------------------------------------------------------------------
ABSTRACT METHOD:

Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class.

Steps to Create Abstract Base Class and Abstract Method:
1. Firstly, we import ABC and abstractmethod class from abc (Abstract Base Class) library.
2. Create a BaseClass that inherits from the ABC class. 
    In Python, when a class inherits from ABC, it indicates that the class is intended to be an abstract base class.
3. Inside BaseClass we declare an abstract method named “method_1” by using “abstractmethod” decorator. 
    Any subclass derived from BaseClass must implement this method_1 method. 
    We write pass in this method which indicates that there is no code or logic in this method.

Syntax:
from abc import ABC, abstractmethod # (Abstract Base Class)
class BaseClass(ABC):
    @abstractmethod # decorator
    def method_1(self): # is a abstract method
        # empty body
        pass

As a property, abstract classes can have multiple abstract methods coexisting with several other methods.
For example:
from abc import ABC, abstractmethod
class abs_class(ABC):
    #normal method
    def method(self):
        #method definition
    @abstractmethod
    def Abs_method(self):
        #Abs_method definition

-------------------------------------------------------------------------------------------------------
CONCRETE METHOD:

Concrete methods are the methods defined in an abstract base class with their complete implementation. 
Concrete methods are required to avoid reprication of code in subclasses. 
For example, in abstract base class there may be a method that implementation is to be same in all its subclasses, 
    so we write the implementation of that method in abstract base class after which we do not need to write implementation of the concrete method again and again in every subclass.

For example: main.py 

To sum up, you can get a abstract class so that the other classes will have some signature or some restriction to words method define.
Example when you define API so you can create a API if someone wants to use your API, they have to define all the methods.