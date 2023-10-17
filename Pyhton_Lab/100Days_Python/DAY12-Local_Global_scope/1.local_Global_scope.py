# Local scope

def drink_potion():
    potion_strength=2
    print(potion_strength)
drink_potion()
print(potion_strength)  # here using the variable potion strength , throughs an error as it is defined inside a function and not defined outside a function

# i.e usability of a variable or function defined inside a function is known as local scope.

# Global scope

player_health=10

def drink_potion():
     potion_strength=2
     print(player_health)  # here using the variable player_strength is completely valid as it is defined outside the function.
drink_potion()    



