print("Welcome to the simple BMI calculator ! ")

height = input("Enter your height in meters \n")

h=float(height)

weight = input("Enter your weight in Kgs \n")

w=float(weight)

BMI = (w/(h)**2)

BMI_as_INT=int(BMI)

print("your BMI is ",BMI)

