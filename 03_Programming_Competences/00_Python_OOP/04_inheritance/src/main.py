'''Python Inheritance'''
class Employee:
    '''Base class'''
    def __init__(self, id, name: str):
        self.id = id
        self.name = name

# Here we declare that the Salary class inherits from the Employee class
class Salary(Employee):
    '''Salary is a derive class from base class Employee'''
    def __init__(self, id, name, salary):
        super().__init__(id, name) # super() function allows we to call the superclass | baseclass's methods
        self.salary = salary