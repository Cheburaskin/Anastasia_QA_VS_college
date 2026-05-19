"""n=10
while n > 0:
    print("n is:", n)
    n = n-1

n=1
while n < 10:
    print("n is:", n)
    n += 1
"""
#for i in range(1, 10, 3): #  range(start, stop, step)  
 #   print("i is:", i)  
for i in range(1, 51): #  range(start, stop, step)  
    if i%2 == 0:
        print("i is even:", i)
    else:
        print("i is odd:", i)
