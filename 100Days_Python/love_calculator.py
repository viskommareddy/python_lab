print('Welcome to love calcualtor!')
name1=input('enter the name of the first person: ')
name2=input('enter the name of the second person: ')
combined_name=name1+name2
combined_name_lower=combined_name.lower()
t=combined_name_lower.count('t')
r=combined_name_lower.count('r')
u=combined_name_lower.count('u')
e=combined_name_lower.count('e')
true=(t+r+u+e)
l=combined_name_lower.count('l')
o=combined_name_lower.count('o')
v=combined_name_lower.count('v')
e=combined_name_lower.count('e')
love=(l+o+v+e)
score=int(str(true)+str(love))
if score<=10 or score >=90:
    print(f'your love score is {score} and you go to geather like coke and mentos')
elif score>=40 and score<=50:
    print(f'your love score is {score} and you are alright togeather')
else:
    print(f'your love score is {score}')