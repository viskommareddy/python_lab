
"""
# arguments

def add(n1,n2):
    return n1+n2
add(n1=5,n2=3)


# unlimited arguments

def add(*args): # * implies unlimited arguments are accepted and no need to stick to the word args
    print(type(args))
    print(args[1]) # this prints the argument at a particualr index 1  --- as this is a positional argument 
    sum =0
    for n in args:    # note ,that these arguments(args) are  stored in the form of a 'tuple' and for loop loops through all the arguments
        sum +=n     # then we can do what ever we want to with that arguments       
    return sum

print(add(3,5,6,7))

"""
def calculate(**kwargs): # ** implies unlimited keyword arguments are accepted,note thast * is for unlimited positional arguments only 
    print(type(kwargs))       # the keyword arguments are stored in the form of a dictionary
    for key,value in kwargs.items():
        print(key)
        print(value)
    


def calculate(n,**kwargs):    # ** implies unlimited keyword arguments are accepted,note thast * is for unlimited positional arguments only 
    print(type(kwargs))       # the keyword arguments are stored in the form of a dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n
print(calculate(2,add=3,multiply=5))
    











   
