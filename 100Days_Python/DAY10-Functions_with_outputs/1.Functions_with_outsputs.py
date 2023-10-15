def my_function():
    result=3*2
    return result

my_function()  # here the result is returned to the my_function(), when ever it is called.

a=my_function()

print(a) 

#example 2

def format_name(f_name,l_name):
    f_f_name=f_name.title()
    f_l_name=l_name.title()
    return  print(f"{f_f_name} {f_l_name}")

print(format_name("viSHnu","koMMaReddy"))  # the returned result will be retrived when ever we call the function.

# Multiple return values
#example

def your_name(f_name,l_name):
    """Take the first name and last name to 
    to return the title version of the same."""   # this is a doc string """  """. since it is inside a function, it gives the description of the function , when hovered on the called function.if it is out side the function, it acts as a multi line comment.
    if f_name=="" or l_name=="":
        return "you haven't provided a valid input"
    f_f_name=f_name.title()
    f_l_name=l_name.title()
    return (f"{f_f_name} {f_l_name}")

print( your_name( input( "Enter your first name:" ),input( "Enter your last name:" ) ) )# calling the function.

# Recursion

"""calling a function with in , same function is called as a recursion"""

#example
def hello():
    print("world")
    hello() # since function hello is called inside the same hello function,it is called recursion.
hello()

# we can set flags to make use of the same in while loops, inside functions.