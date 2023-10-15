import random

import my_module # we can import the module which we created and use them here.

random_integer = random.randint(0,100)

print(random_integer)

print(random_integer*my_module.pi)

random_float=random.random() #it gives a float b/w 0 to 1
print(random_float)

love_score = random.randint(0,100)
print(f"your love score is {love_score}")