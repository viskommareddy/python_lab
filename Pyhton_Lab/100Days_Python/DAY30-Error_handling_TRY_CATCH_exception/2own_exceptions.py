# we can raise our own errors and exceptions
"""
try:
    file=open("a_file.txt")
    a_dictionary={"key":"value"}   # her there are multiple tries
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:  #exception related to FileNotFoundError
    file=open("a_file.txt")
    file.write("something")
except KeyError as error_message: #exception related to KeyError, here we are holding the error message to pss it in the print statement
    print(f"That key {error_message} does not exist.")
else:# this block executes only when no exceptio is found in the try block else the except block gets executed if there is any exception found in the try block
    content=file.read()
    print(content)
finally:  # here the exception has been raised to crash with an error and message
    raise TypeError("this is an error i made up")
    """

# to understand what cases we use raising an exception follow the below example

height=float(input("height:"))
weight=int(input("weight:"))

# if the height provided is unrealistic,like 35 mts which is odd,then we can raise an error 
if height>3:
    raise  ValueError("the height you have entered is unrealistic, please check")

bmi=weight/height**24

print(bmi)




