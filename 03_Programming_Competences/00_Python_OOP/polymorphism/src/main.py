'''Function Overloading (FO) Introduction by Indently https://www.youtube.com/@Indently'''
from functools import singledispatch, singledispatchmethod
from typing import Any 


# FO Implementation on function
@singledispatch
def func(arg: Any, verbose=False):
    # The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
    raise NotImplementedError(f"Type:{type(arg)} is not a valid type for this function")

# now we can register which type of the argument could be implemented into the function that is defined as above 
@func.register
def _(arg: int | float, verbose=False):
    if verbose:
        print(f"Your Number Is {arg}")
        return
    print(f"Number: {arg}")

@func.register
def _(arg: str, verbose=False):
    if verbose:
        print(f"Your Text Is {arg}")
        return
    print(f"Text: {arg}")

if __name__ == "__main__":
    # func(['69',69],verbose=False)
    func("Testing...",verbose=True)
    func(69,verbose=False)