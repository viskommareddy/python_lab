print('Welcome to the roller coaster!')
height=int(input('enter your height: '))
if height >=120:
    age=int(input('enter your age: '))
    if age <=12:
        bill=5
        print('chrildrens ticket is $5')
    elif age<=18:
        bill=7
        print('youth ticket is  $7')
    elif age>=45 and age<=55:
        print('cool, your ticket has been taken care by us,enjoy your ride.')
    else:
        bill=12
        print('general ticket is $12')

    photo=str(input('do you want ypur photo? choose Y/N : '))
    if photo=='Y':
        bill+=3
        print(f'your final bill is ${bill}')


else:
    print('come back once you grow taller.')