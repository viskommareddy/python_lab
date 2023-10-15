#round
print(8/3)

print(round(8/3,2)) # rounds the result to the number of decimals specified after the comma.

print(8/2) # it gives 4.0 as a result instead of 4

print(type(8/2))  # single / all ways gives the result as a float , even though it is a clean division.

print(type(8//3)) # // gives an int instead of float

result=(4/2)
# for continuous operations,
result /= 2 # this is helpful replace result =result/2 , it could behandy in loops
print(result)

# another example
score =0
score +=1 # this is helpful to replace score = score+1 , it could be handy in loops
print(score)

# f-string
score=1
height=1.8
iswinning=True

# in order to use all the data types in a single string in this case, an f string is helpful

print(f"your score is {score},your height is {height},your winning is {iswinning}")






