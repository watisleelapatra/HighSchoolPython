#calculate average value
Sum, x = 0, 0
i = 0
while x >= 0 :
    x = float(input("Enter a positive number "))
    Sum = Sum + x
    i = i + 1
Sum = Sum - x
i = i - 1
avg = Sum/i
print("Sum of all numbers = " +str(Sum))
print("Total numbers = " + str(i))
print("Average = " + str(avg))