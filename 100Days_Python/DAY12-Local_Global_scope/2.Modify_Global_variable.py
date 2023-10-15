
# Modify a Global variable

# note the difference b/w usinfg a global variable inside a function and modifying it.

enemies = 1

def increase_enemies():
    enemies+= 1  # this is not using the variable, this is modifying a global variable by increment.
    print(f"Enemies inside function : {enemies}")
    
increase_enemies()

"""This code gives an error , as enemies is declared globally and not inside the function,
the function assumes that the enemies variable is being modified with out previously declaring it"""

"""hence we need to mention inside the function that it is a global variable, which is already declared,
inorder to moidify it."""

"""note that a global variable can be used , in side a function wiht out refering it is global.
but for mdifying the same like increment, it needs to be refered as a global variable inside the function"""

enemies = 1

def increase_enemies():
    global enemies # refering the variable as variable , before modifying the variable, in the next line 
    enemies+= 1
    print(f"Enemies inside function : {enemies}")
    
increase_enemies()

"""this chunk of code executes, wiht out any error."""


"""the same o/p as above can be obtained with out reference as a global variable, by using return"""
# note that here , we are not modifying the global variable, but using a return with increment.

enemies = 1

def increase_enemies():
    print(f"Enemies inside function : {enemies}")
    return enemies + 1


increase_enemies()
# this chunk of code gives the same o/p as previous chunk of code.
