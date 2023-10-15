print("Welcome to the BMI calculator !")

N   =   input("Enter your name \n")
H   =   float( input (f"Enter your height in meters {N}\n" ) ) 
W   =   float( input (f"Enter your weight in Kgs {N} \n") )
B = round(W/H**2 , 2)

if B < 18.5:
    print(f"{N},your BMI is {B} and you are  under weight.")
elif B<=25:
     print(f"{N},your BMI is {B} and you have a normal weight.")
elif B<=30:
     print(f"{N},your BMI is {B} and you are  Over weight.")
elif B<=35:
     print(f"{N},your BMI is {B} and you are obese")
else:
     print(f"{N},your BMI is {B} and you are clinically obese.")



