x = 1
x_p = 1
sum = 0

while (x < 4_000_000):
    
    x += x_p
    x_p = x - x_p
    if(x%2==0):
        sum += x

print(sum)

    
   

