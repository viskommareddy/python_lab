print("welcome to the leap year finder!")

Y=int(input("Enter the year which you want to check."))

if (Y % 4 == 0) :
    
    if (Y % 100 == 0) :
        
        if(Y % 400 == 0) :
            
            print (f"{Y} is a leap year.")
        else:
            print(f"{Y},is not a leap year.")
    else:
        print(f"{Y},is a leap year.")
else:
    print (f"{Y} is not a leap year.")
            
        
    
    