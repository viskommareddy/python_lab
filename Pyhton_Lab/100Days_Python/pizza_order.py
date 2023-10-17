print("welcome to vishnu's pizza!\nPlease enter your choice below")
size=input('what is the size you want ? S || M || L : ')
s=['S','M','L']
c=['Y','N']
if size in s:
    add_pepperoni=input('Do you want pepperoni ? Y || N : ')
    if add_pepperoni in c:
        extra_cheese=input('Do you want extra cheese ? Y || N : ')
        if extra_cheese in c:
            bill=0

            if size=='S':
                bill+=15
                if add_pepperoni =='Y':
                    bill+=2
                if extra_cheese =='Y':
                    bill+=1
            elif size=='M':
                bill+=20
                if add_pepperoni=='Y':
                    bill+=3
                if extra_cheese=='Y':
                    bill+=1
            elif size=='L':
                bill+=25
                if add_pepperoni=='Y':
                    bill+=3
                if extra_cheese=='Y':
                    bill+=1

            print(f'the total order amount = $ {bill}')


        else:
            print('Thats an invalid choice, plz try again. ')
    else:
        print('Thats an invalid choice, plz try again. ')
else:
    print('Thats an invalid choice, plz try again. ')

    




