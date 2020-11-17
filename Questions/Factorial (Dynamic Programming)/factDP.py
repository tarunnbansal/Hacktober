from collections import defaultdict

memo=defaultdict(lambda:None)

def factorial(n):
    if memo[n] != None:
        pass
    elif n<2:
        memo[n]=1
    else:
        memo[n]=n*factorial(n-1)
    return memo[n]

num=int(input("Enter the number : "))
print('Factorial of',num,'is :',factorial(num))
