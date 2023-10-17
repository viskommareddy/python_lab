print("welcome to simple Tip Calculator\n")
bill=float(input("Enter the bill amount : $ "))
tip=int(input("Enter the percentage of Tip which you want to give : 12 / 15 or 18 : "))
people=int(input("Enter the number of people : "))
tip_perc=tip/100
tip_amt=bill*tip_perc
total_bill=bill+tip_amt
per_head=round(total_bill/people,2)
print(per_head)
# though we have specified the number of digits after the decimal as 2, it is just returning 1 digit
#so need to use a specific format
per_head=("{:.2f}".format(per_head))
print(f"Each person should pay $ {per_head}")

