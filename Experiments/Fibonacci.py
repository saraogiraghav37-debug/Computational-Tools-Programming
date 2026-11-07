#Fibonacci series using recursion

def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

def series(terms):
    for i in range(terms):
        print(fibonacci(i),end=' ')

terms = int(input("Enter no. of terms: "))
print("Fibonacci Series: ")
series(terms)