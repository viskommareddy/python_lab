print("welcome to vishnu's prime number check.")

def prime_num_check(number):
    is_prime=True
    if number==1:
        is_prime=False
    for i in range(2,number): # note that the upperlimit in range is not inclusive    
        if number%i==0:
           is_prime=False
    if is_prime:
        print(f"{number} is a prime number🙌.")
    else:
        print(f"{number} is not a prime number👌." )
prime_num_check(
    number=int(input("enter the number you want to check:"))
    )

# prime check till the given numbers:

upto_num=int(input(f"enter the number upto which we need to check the prime numbers:"))
for i in range(2,upto_num+1):
    prime_num_check(i)





