# assigning the input data to a variable
name=input('What is your name?')
# Printing the variable
print(name)
# if assign another data to the same variable, it stores the latest data and ignores the prwvious one.
a='vishnu'
a='jack'
print(a) # it prints jack instead of vishnu as the variable is updated eith the name jack now.

#using input,variable and length
name=input('What is your name?')
length=len(name)
print(length)

#variable swaping excercise

a=3
b=5
c=a             # assigning the data stored in a to c.
a=b             # assigning the data stored in b to a ,now a has the value of b.
b=c             # assigning the data stored in c to b, which is nothing but the initial data stored in a .
print(a ,b)     # now the result should print the values of a,b after the swapping is done.

# naming the variables
username='vishnu'
user_name='vishnu' # this is the best practice to use _ to separate words in a variable.Never use space in b/w
# never use function names as variable names.

