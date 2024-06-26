'''Python Encapsulation'''

# Python program to demonstrate protected members 
  
# Creating a base class 
class Base: 
    def __init__(self):   
        # Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated.  
        self._a = 'Base Protected Member' 
        # Protected member are defined by prefixing the name of the member by a single underscore “_”
        self.__a = 'Base Private Member'
        # Private member are defined by prefixing the member name with double underscore “__”.
  
# Creating a derived child class 
class Derived(Base): 
    def __init__(self): 
  
        # Calling constructor of Base class 
        Base.__init__(self) 
        # print("Calling protected member of base class: ", self._a)
        # print("Calling private member of base class: ", self.__a) -> AttributeError: 'Derived' object has no attribute '_Derived__a'
  
        # Modify the protected variable: 
        self._a = 'Modified Protected Member'
        # print("Calling modified protected member outside class: ", self._a) 
        # Modify the private variable:
        # self.__a = 'Modified Private Member'
        # print("Calling modified private member outside class: ", self.__a) -> AttributeError: 'Derived' object has no attribute '_Derived__a'

# Example of calling the private and set condition for calling it from NeuralNine
class Person:
    def __init__(self, name, age, gender):
        # set these attributes to private
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property # make the method below a property 
    def PrintName(self): # the method
        '''Returns the private member '__name' of the Person class'''
        return self.__name # return as an attribute

    @PrintName.setter # simple syntax for setting the condition for PrintName method, this is possible after making the method a property as above
    def PrintName(self, value):
        if value == 'MGK':
            self.__name = 'Marshall Mathers'
        else:
            self.__name = value
    
    @staticmethod # This used to define statics method below
    def static_method():
        '''STATIC METHODS are methods within a class that have no access to anything else in the class (no self keyword or cls keyword). 
        They cannot change or look at any object attributes or call other methods within the class. 
        They can be thought of as a special kind of function that sits inside of the class.'''
        print('I am an independable method !')

if __name__ == '__main__':
    # obj1 = Derived() 
    # obj2 = Base() 
    p1 = Person('Hung', 26, 'male')
    # p1.PrintName = 'MGK'
    # print(p1.PrintName)
    p1.static_method()
    Person.static_method()
    # print(obj2.__a) -> AttributeError: 'Base' object has no attribute '__a'. Did you mean: '_a'?

    # Calling protected member Can be accessed but should not be done due to convention 
    # print("Accessing protected member of the derived class obj1: ", obj1._a) 
    
    # Accessing the protected variable outside 
    # print("Accessing protected member of the base class obj2: ", obj2._a) 