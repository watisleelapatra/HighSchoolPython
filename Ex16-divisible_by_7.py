#Program to find numbers divisible by 7
n = 0
while n <= 100 :
    if n % 7 == 0 :  #remainder must be 0 if divisible
        print(n)
    n = n + 1