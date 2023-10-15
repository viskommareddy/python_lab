#type check
num_char=len(input("what is your name ? \n"))
print(type(num_char))

#type conversion / type casting
char=str(num_char)
print(type(char))
print("your name has "+" "+char+" "+"characters") #now there wont be any type error for concatination.

a=123
print(type(a))

b=str(a)
print(type(b))

c=int(b)
print(type(c))

print(70+float("30.5")) # addition because of int and float data types

print(str(70)+str(100))# concatination because of str data types


