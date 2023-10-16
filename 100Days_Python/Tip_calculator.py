print('welcome to the tip calculator!')
bill_amount=float(input('enter the bill amount: $ '))
tip_percentage=int(input('choose the tip % :- 0 or 10 or 15 or 18 : '))
total_bill=bill_amount+(bill_amount*tip_percentage/100)
persons=int(input('enter the number of people to split the bill : '))
share=total_bill/persons
print(f"the total bill is : $ {total_bill}\neach person's share is : $ {round(share,2)}")