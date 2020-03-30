def check_prime( x ):
    for i in range(2,x-1):
        if(x%i==0):
            return False
    return True

primes = []
i = 1
while(len(primes)<=10001):
    if(check_prime(i)):
        primes.append(i)
    i+=1

print (primes[10001])
