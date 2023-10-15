for number in range(1,101):
    if number%3==0 and number%5==0: #divisible by both 3 and 5 , then its a fizz buzz
        print('fizzbuzz')
    elif number%5==0:               #divisible by 5 alone , then its buzz
        print('buzz')
    elif number%3==0:               #divisible by 3 alone, then its a fizz
        print('fizz')
    else:
        print(number)