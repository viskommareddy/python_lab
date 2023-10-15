# note that the input data is by default considered as a str, though it is a number.

num=input("Enter a two digit number:\n")
print(type(num))
# note that we can not subscript int data types but str data types.
answer=int(num[0])+int(num[1])
print(type (answer))
print('The answer is ',answer)
