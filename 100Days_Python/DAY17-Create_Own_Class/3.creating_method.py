class User():
    def __init__ (self,user_id,user_name):
        self.id=user_id
        self.username=user_name
        self.followers=0 # note that, we can initialize a variable, with out settiong it to a parameter to be passed and assigining it to a value instead as per need.
        self.following=0
        
    def follow(self,user):
        user.followers=+1  # user is the user who is being followed
        self.following=+1  # self is the user who follows

user_1=User("001","vishnu")
user_2=User("002","Reddy")

user_1.follow(user_2)

print(user_2.followers,user_2.following)
print(user_1.followers,user_1.following)
