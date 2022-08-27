#factorial
n = int(input("Enter a number n : "))
factorial = 1
for i in range(1, n+1) :
    factorial = i*factorial

print(n, end = '')
print("! = ", end = '')
print(factorial)
