def check_prime(number):
    if(number == 2 or number ==3 or number ==5 or number == 7):
        return True
    # if int(number**0.5) == 2:
    #     return False
    for factor in range(2,int(number**0.5)+1):
        if(number % factor == 0):
            return False
    return True


sum = 0
for counter in range(2,2000001):
    if(check_prime(counter) == True):
        sum += counter

print(sum)