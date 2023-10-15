print("Welcome to the roller coaster ride!")
h=int(input("Enter your height in Cms: "))
if h>120:
    a=int(input("Enter your age : "))
    print("Welcome abord! you can puchase the ticket now .")
    if a<12:
        bill=5
        print("Please pay $ 5")
    elif a<=18:
        bill=7
        print("Please pay $ 7")
    else:
        bill=12
        print("Please pay $ 12")
    p=input("Do you want a photo ? : Y or N\n")
    if p=="Y":
        bill +=3
        print(f"The total bill is ${bill},Proceed for the payment.")
    else:
        print("ok you can proceed for the payment.")
else:
    print("sorry, you need to grow your height more to ride the roller coaster.")