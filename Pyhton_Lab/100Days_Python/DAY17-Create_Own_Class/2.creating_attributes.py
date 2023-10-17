# construct / Initialize
class User:
    def __init__(self) :
        print("new user being created..")
        
user_1=User()
user_1.id="001"
user_1.name="vishnu"
print(user_1.name)
# so each time a new user is createed, the statemenrt new user being created , prints, as initialized above
user_2=User()
user_2.id="002"
user_2.name="kommareddy"
print(user_2.name)

# initializing an attribute
class Car:
    def __init__ (self,seats): # here seats is an attribute of Car class.
        self.seats =seats
        
my_car=Car(5) # object my_car created from the class Car

print(my_car.seats) # we can check the initialization of the attribute seats , for the object my_car
        
# further, for creating a lot of objects having the same attributes 
# ----basically we are initializing the attributes to the class, before creating the objects which have the same attributes

class User():
    def __init__ (self,user_id,user_name):
        self.id=user_id
        self.username=user_name
        self.followers=0 # note that, we can initialize a variable, with out settiong it to a parameter to be passed and assigining it to a value instead as per need.
        self.following=0
        
user_1=User("001","vishnu") # 001, is the user_id and vishnu is the user name
user_2=User("002","Reddy")  # 002 and Reddy are the id and name respectively
user_3=User("003","kommareddy")

print(user_3.id,user_1.username,user_2.followers) #here we get the user id of the user_3 and the usdre name of the user_1

# creating methods
# any fuction associated with an object is known as a method.

def follow(self,user):
    user.followers=+1  # user is the user who is being followed
    self.following=+1  # self is the user who follows

user_1.follow(user_2)

print(user_2.followers,user_2.following)
print(user_1.followers,user_1.following)

    