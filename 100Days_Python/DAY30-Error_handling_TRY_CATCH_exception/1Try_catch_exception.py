# File not Found
# with open("a_file.txt") as file:
#   file.read()


#keyerror
# a_dictionary = {"key":"value"} 
# value = a_dictionary["non_existant_key"]

#indexerror
#fruitlist=["apple","banana","pear"]
#fruit=fruitlist[3]

#type error
#text = "abc"
#print(text+5)


"""
syntax

try:
    something that might cause an exception
except:
    do this if there was an exception
else:
    do this if there is no exception
finally:
    do this no matter what happens


this is done to not stop the programming script due to an error which could be expected ,so we
give an exception of what to do incase there is a scope for an error and rectify it in the exception itself
its like auto repair with out stopping

"""

# example

try:
    file=open("a_file.txt")  # it tries if the file is existing ?
except:
    file=open("a_file.txt","w") # if the file is not existing when tried , then a new file is created as per the exception here, to avoid the error
    file.write("something")# this writes the text "something" into the file created.
    

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
finally: 
    file.close() # this closes the file even if it suceeds to read the file or fails ot read the file
    print("File was closed")
