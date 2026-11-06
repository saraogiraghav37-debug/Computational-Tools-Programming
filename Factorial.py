#Calculate factorial of a number and check whether it is prime

import math
num = int(input("Enter a number: "))

#Factorial Calculation
def factorial(num):
    fact = 1
    if num<0:
        return 0
    else:
        for i in range(1,num+1):
            fact*=i
        return fact

#Prime number checking
def isPrime(num):
    if num<2:
        return False
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True
if(factorial(num)):
    print("Factorial of",num,"is",factorial(num))
else:
    print("Factorial of negative numbers does not exist")

if(isPrime(num)):
    print(num,"is prime")
else:
    print(num,"is not prime")