#function
'''
def my_function():
    #do this
    #then do this 
    #finally do this

my_function()
'''
#Example_Function:
def greet():
    print('Hello')
    print('How do you do today')
    print("isn't the weather good today?")

greet()

#functions with inputs
'''
def my_function(something):
    #do this with 'something'           here , something becomes 123 
    #then do this                       something is called as parameter and
    #finally do this                    123 is called as argument

my_function(123)
'''

#example_functions with inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}")
    print(f"{name},isn't the weather good today ?")

greet_with_name(input("enter your name:"))

#functions with more than one input

#example_functions with more than one input

def greet_with(name,location):
    print(f"Hello,{name}")
    print(f"what is it like in {location}")
greet_with(input("enter your name:"),input("enter your location:"))

#positional arguments
'''
def my_function(a,b,c):
    #do this with 'a'
    #do this with 'b'
    #do this with 'c'
my_function(1,2,3)              ---- this implies that a='1',b='2',c='3', so the order of the arguments matter in this case.
'''
#keyword arguments
'''
def my_function(a,b,c):
    #do this with 'a'
    #do this with 'b'
    #do this wiht 'c'
my_function(c=3,a=1,c=2)        --------the order of the arguments doesn't matter in this case, as the arguments are assigned to the parameters.

'''
#example_keyword arguments

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"what is it like in {location}")
greet_with(location=input('enter the name of the location:'),name=input('enter your name:'))



