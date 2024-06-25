'''
Function Overloading (FO) Tutorial by Indently https://www.youtube.com/@Indently
Operator Overloading (OO) Tutorial by Telusko https://www.youtube.com/@Telusko
'''
from functools import singledispatch, singledispatchmethod
from typing import Any 

############################################################
# FO Implementation on function

@singledispatch
def func(arg: Any, verbose=False):
    # The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
    raise NotImplementedError(f"Type:{type(arg)} is not a valid type for this function")

# now we can register which type of the argument could be implemented into the function that is defined as above 
@func.register
def _(arg: int | float, verbose=False):
    if verbose:
        print(f"Your Number is {arg}")
    else:
        print(f"Number: {arg}")

@func.register
def _(arg: str, verbose=False):
    if verbose:
        print(f"Your Text is {arg}")
    else:
        print(f"Text: {arg}")

############################################################
# FO Implementation on class
class Computer:
    @singledispatchmethod
    def display(self, arg: Any, verbose=False) -> Any | None: # verbose meanning for long 
        if verbose:
            result = 'Computer Displaying ' + str(arg)
        else:
            result = arg 
        print(result)

    @display.register(str)
    def _(self, arg, verbose=False) -> str:
        if verbose:
            result = 'Computer Displaying ' + str(arg)
        else:
            result = arg 
        print(result)

    @display.register(int | float)
    def _(self, arg, verbose=False) -> int | float:
        if verbose:
            result = 'Computer Displaying ' + str(arg)
        else:
            result = arg 
        print(result)

    @display.register(list)
    def _(self, arg, verbose=False) -> list:
        if verbose:
            result = 'Computer Displaying ' + str(arg)
        else:
            result = arg 
        print(result)


############################################################
# OO Implementation on class
class Number:
    def __init__(self,number_1: int | float, number_2: int | float) -> None:
        self.number_1 = number_1
        self.number_2 = number_2
    def __add__(self,value) -> object | None:
        number_1 = self.number_1 + value.number_1
        number_2 =self.number_2 + value.number_2
        n3 = Number(number_1, number_2)
        return n3 
    
if __name__ == '__main__':
    n1=Number(2,3)
    n2=Number(3,5)
    n3=n1 + n2
    print(n3.number_2)