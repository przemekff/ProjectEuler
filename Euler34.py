def factorial(x):
    if x == 1 or x == 0:   
        return 1
    return x*factorial((x-1))

def check_curious(x):
    number = str(x)
    sum = 0
    for i in range(len(number)):
        sum += factorial(int(number[i]))
    if (sum == x):
        return True
    return False

def find_range():
    i = 1
    #maximum sum of factorials is sum of all 9's
    #if this sum is smaller than the smallest number in this range, then there are no curious numbers
    while(factorial(9)*i >= 10**i-1 ):
        i+=1
    return i 


lst = []
sum = 0
for i in range(10**find_range()):
    if(check_curious(i)):
        sum += i 
print(sum - 3)

