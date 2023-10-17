import random
states_of_america = ["arizona","alabama","alaska","arkansas","connecticut","colorado","delaware",
                     "north dakota","south dakota","nebraska","oklahoma","ohio","new mexico","rhode island"
                     "virginia","west virginia","wyoming","idaho","iowa","illinois","indiana","georgia",
                     "masachusetts","new hampshire","new jersey","new york","texas","kentucky","missouri","lousiana",
                     "Tennesse","california","utah","washington","oregon","maryland","north carolina","south carolina"
                     "minnesota","florida","hawai","maine","nevada","michigan","wisconsin","kansas","missisipi","montana",
                     "pennsylvania","vermont"]
print(len(states_of_america))

print(states_of_america[0:5]) # prints 0,1,2,3,4

print(states_of_america[-1]) # prints from the last 1

states_of_america.append("vishnuland") # for single item or list , we dont use []

print(states_of_america)

print(states_of_america[-1])

states_of_america.extend(["myland","yourland"]) # for multiple items, we use []

print(states_of_america)

new_string=input("enter all the names separated by a comma\n")

new_list=(new_string.split(","))

print(new_list)

a=(new_list [ random.randint( 0,len( new_list )-1) ] )

print(f"{a} is going to pay for the lunch today.")

# we can use random.choice(new_list) , which is more simple ,than using indices
# if we use insert attribute for a list, it will replace the item in the index mentioned.