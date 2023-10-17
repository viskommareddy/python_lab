print("welcome to python pizza 🍕🍕🍕!")
name=input("Enter your name:\n")
size=input("Please select the size of the pizza you want : S or M or L \n")
if size=="S":
    amt=15
elif size=="M":
    amt=20
elif size=="L":
    amt=25
pep=input("Do want papperoni🔴 add on ? Y or N\n")
if pep=="Y" and size=="S":
    amt +=2
elif pep=="Y" and (size=="M" or size=="L"):
    amt +=3
cheese=input("Do you want cheese 🧀 add on? Y or N\n")
if cheese=="Y":
    amt +=1
print(f"{name},your total bill 💵 is $ {amt}")