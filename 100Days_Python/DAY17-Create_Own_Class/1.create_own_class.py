#syntax
class User:  # the class user has been created
    pass     # if the class or function is empty, python gives indentation error for the next line, so we use pass
             # always note that each word of the class is capital(pascal casing) 
user_1=User() # user_1 is an object created from the class User()

# PascalCase   camelCase   snake_case   ---------- note the difference
# attribute is a variable that is associated with an object

user_1.id="001" # id is an attribute created
user_1.name="vishnu" # name is an attribute created
print(user_1.id,user_1.name)

user_2=User() # another object created from the same class(blue print)
user_2.id="002"
user_2.name="kommareddy"
# constructor is a part of the blue print ,specifies what to happen when objec tisw being constructed
# this is also  known as initializing an object 




