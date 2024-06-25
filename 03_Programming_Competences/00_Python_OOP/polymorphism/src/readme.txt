What is Polymorphism: 
    The word polymorphism means having many forms. 
    In programming, polymorphism means the same function name (but different signatures) being used for different types.
    The key difference is the data types and number of arguments used in function.

Polymorphism
    -> Compile Time
        -> Function Overloading
        -> Operator Overloading
    -> Run Time
        -> Function Overriding

Polymorphism is a property through which any message can be sent to objects of multiple classes, 
and every object has the tendency to respond in an appropriate way depending on the class properties.

-------------------------------------------------------------------------------------------------------
Example of inbuilt polymorphic functions:
# len() being used for a string
print(len("geeks"))
# len() being used for a list
print(len([10, 20, 30]))
# Output:
5
3
--> len() is a polymorphic function 

-------------------------------------------------------------------------------------------------------
Examples of user-defined polymorphic functions: 
def add(x, y, z = 0): 
	return x + y+z
# Driver code 
print(add(2, 3))
print(add(2, 3, 4))
# Output: 
5
9
--> add() is a polymorphic function

-------------------------------------------------------------------------------------------------------
FUNCTION OVERLOADING:

Definition: Function overloading refers to the ability to define multiple functions with the same name 
but different parameters or argument types within a programming language.

Example:
