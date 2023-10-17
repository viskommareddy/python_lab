import random
print('welcome to password generator')
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','-','+']
num_letters=int(input('enter the number of letters in the password: '))
num_numbers=int(input('enter the number of numbers in the password: '))
num_symbols=int(input('enter the number of symbols in the password: '))

'''
#easy level--- general level password

password=""
for number in range(1,num_numbers+1):
    random_number=random.choice(numbers)
    password+=random_number
print(password)
for letter in range(1,num_letters+1):
    random_letter=random.choice(letters)
    password+=random_letter
print(password)
for symbol in range(1,num_symbols+1):
    random_symbol=random.choice(symbols)
    password+=random_symbol
print(password)
'''


# hard level--- more secured password--- randomizing the characters in the password, instead of sequence characters

password_list=[]

for number in range(1,num_numbers+1):
    password_list.append(random.choice(numbers))
for letter in range(1,num_letters+1):
    password_list.append(random.choice(letters))
for symbol in range(1,num_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print(f'here you go, your password is {password}')