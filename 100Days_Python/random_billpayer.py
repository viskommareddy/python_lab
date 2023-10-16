
# with out using a choice()
'''
import random
names=input('enter all the names followed by a comma : ')
name=names.split(',')
number_persons=len(name)
number_choice=random.randint(0,number_persons-1)
person=name[number_choice]
print(f'the person who is paying to day is {person}')
'''
# using the choice()

import random
names=input('enter all the names followed by a comma :')
name=names.split(',')
payer=random.choice(name)
print(f'the one who is going to pay the bill is,{payer}')



