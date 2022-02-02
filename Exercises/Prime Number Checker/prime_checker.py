def checker(number):
    c=0     #is_prime=True
    for i in range(2,(number-1)):
        result=number/i
        if (result*10)%10==0:
            c=c+1   #is+prime=False
    if c>0: #is_prime=False
        print(f"{number} is not prime")
    else:
        print(f"{number} is prime")
