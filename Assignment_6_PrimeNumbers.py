n = int(input("Enter a number: "))  
prime_num = []  
if n > 1:
    for j in range(2,n+1):
       for i in range(2,j):  
           if (j % i) == 0:  
               break  
       else:  
           prime_num.append(j)
else:  
   print(j,"is not a prime number")
print(prime_num)
