print('Welcome to BMI Calculator!')
height=float(input('Enter your height in meters:'))
weight=int(input('Enter your weight in Kgs:'))
BMI=weight/(height**2)
print('your BMI is ', BMI)
if BMI <18.5:
        print('watch out, you are Under weight')
elif BMI <=24.9:
        print('your BMI is Normal')
elif BMI <=29.9:
        print('watch out, you are Over weight')
elif BMI <=34.9:
        print('watch out , your BMI falls under obesity class-1')
elif BMI<=39.9:
        print('watch out , your BMI falls under obesity class 2')
else:
        print('watch out, your BMI falls under Extreme obesity')
weight_req_min=18.5*(height**2)
weight_req_max=24.9*(height**2)
if weight>weight_req_max:
        print( f'you should not exceed a max of {weight_req_max} kgs of weight,to have a normal BMI')
        print(f'you need to loose {weight-weight_req_max} kgs ')
elif weight<weight_req_min:
        print( f'you need to maintain atleast a min of {weight_req_min} kgs of weight,to have a normal BMI')
        print(f'you need to gain {weight_req_min-weight} kgs ')
