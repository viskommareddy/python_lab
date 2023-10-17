

""" 
car=CarBlueprint()
 
Here car is an object and CarBluepirnt() is a Class and there wont be any _ in the naming of class and
a class will be in pascal casing instead as shown above. 
 
"""
import another_module #another_module is a module

print(another_module.another_variable) #another_variable is a variable

"""
import turtle #turtle is a module for graphics

timmy=turtle.Turtle()  # Turtle is a class , timmy is an object, turtle is a module
"""
 
# this can be simplified further as below
 
from turtle import Turtle,Screen # from turtle module, importing the Turtle class

timmy= Turtle() # creating the object timmy from the class Turtle

print(timmy) # it creates the object in the computer memory.
timmy.shape("turtle")#shape is a method
timmy.color("teal")
x=True
while x== True:
    timmy.forward(100)
    timmy.color("red")
    timmy.left(180.0)
    timmy.color("blue")
    timmy.forward(100)

my_screen=Screen()
print(my_screen.canvheight) # my_screen is the object and canvheight is the attribute

# any function corresponding to an object is called as a method
# calling a function associated with the object , is of the same syntax of calling an attribute

my_screen.exitonclick() # this is a method


#note: class is nothing but a blue print , using which object is created.
