'''Python Abstraction'''
# Import required modules 
from abc import ABC, abstractmethod 
    
# Create Abstract base class which can have multiple abstract function
class Car(ABC): 
    def __init__(self, brand, model, year): 
        self.brand = brand 
        self.model = model 
        self.year = year 
    
    # Create abstract method     
    @abstractmethod
    def printDetails(self): 
        pass # meaning we dont have anything in this function 
     
    # Create concrete method 
    def accelerate(self): 
        print("speed up ...") 
    
    def break_applied(self): 
        print("Car stop") 
    
# Create a child class 
class Hatchback(Car): 
    
    # Hatchback is the child class of the Car BaseClass so we have to write the implementation of the abstract function 
    def printDetails(self): 
        print("Brand:", self.brand); 
        print("Model:", self.model); 
        print("Year:", self.year); 

    def Sunroof(self): 
        print("Not having this feature") 
    
# Create a child class 
class Suv(Car): 

    # Suv is the child class of the Car BaseClass so we have to write the implementation of the abstract function 
    def printDetails(self): 
        print("Brand:", self.brand); 
        print("Model:", self.model); 
        print("Year:", self.year); 
    
    def Sunroof(self): 
        print("Available") 
    
if __name__ == '__main__':
     car1 = Hatchback("Maruti", "Alto", "2022"); 
     car1.printDetails()
     car1.accelerate() # car1 is an instance of the Hatchback child class of car class so it can inherited the base class concrete function