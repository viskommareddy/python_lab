import turtle # keyword-- import   , module name-- turtle

tim = turtle.Turtle() # tim-- object , turtle-- module name, Turtle-- class


# simplified way

from turtle import Turtle #from--keyword  turtle --module  import-- keyword  Turtle -- thing in the module, here it is class

tim =Turtle() # due to the above format of import, we dont need to write turtle.Turtle() everytime.
tom =Turtle() 
tera=Turtle()

from turtle import * # we can import everything in a module using *
from random import *

forward(100) # forward is a method in turtle module
choice([1,2,3]) # choice is a method in random module

# all these methods of the imported modules work. But, it will be confusing to refer to the modules of these methods in the code.

tim=turtle.Turtle() # this syntax is more expressive and we can easily refer to the module of the method/function.

# Aliasing modules 

import turtle as t # import -- keyword ,turtle-- module, as-- keyword , t-- alias for turtle
tim=t.Turtle() #here the object is created using the alias name of the module

import heroes # if a module is not installed , previously, it needs to be installed using pip install command in the terminal or cmd

print(heroes.gen()) # gen is a function in the module heroes, which generates the name of hte hero

# search for different available packages,modules in Pypi website.
