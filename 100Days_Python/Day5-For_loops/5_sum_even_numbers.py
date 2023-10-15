#method 1- without using step
sum_even_num=0
for number in range(1,101):
    if number%2==0:
        sum_even_num+=number
print(f'the sum of even numbers between 1 to 100 is {sum_even_num}')

#method 2- using step
sum_even_num=0
for number in range(2,101,2):
    sum_even_num+=number
print(f'the sum of even numbers between 1 to 100 is {sum_even_num}')