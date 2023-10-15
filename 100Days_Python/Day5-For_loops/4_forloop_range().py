for number in range(1,10): #it doesn't include 10 in range() here, but it includes in random
    print(number)
#so if we need 10 there , then we need to put 10+1 that is 11 there
for number in range(1,11):
    print(number)
#step
for number in range(1,11,3):
    print(number) #this print 1,4,7,10 as we used 3 as step , which takes a step size of 3