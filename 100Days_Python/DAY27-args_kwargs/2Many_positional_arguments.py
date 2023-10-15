
"""
# arguments

def add(n1,n2):
    return n1+n2
add(n1=5,n2=3)
"""

# unlimited arguments

def add(*args): # * implies unlimited positional arguments are accepted and no need to stick to the word args
    print(type(args))
    print(args[1]) # this prints the argument at a particualr index 1  --- as this is a positional argument 
    sum =0
    for n in args:    # note ,that these arguments(args) are  stored in the form of a 'tuple' and for loop loops through all the arguments
        sum +=n     # then we can do what ever we want to with that arguments       
    return sum

print(add(3,5,6,7))










   