import random
#for random integers
random_integer=random.randint(1,100)         # these integers are inclusive
print(f'random integer={random_integer}') 
#for random float numbers
random_float=random.random()    #random() function generates the flot numbers between 0 and 1, excluding 1 
print(random_float)#o/p is b/w 0.0000 to 0.99999. if e=want to increase the range, we can multilply with an integer
randomfloat_mul=random_float*5
print(randomfloat_mul)#o/p is b/w 0.0000.. to 4.999....
