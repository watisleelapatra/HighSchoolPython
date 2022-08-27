#sum of numbers
startnum = int(input("Enter starting number : "))
endnum = int(input("Enter ending number : "))
sum = 0
for n in range(startnum, endnum+1) :
    sum = sum + n
print("Sum of numbers from ", end = '')
print(startnum, end = '')
print(" to ", end = '')
print(endnum, end = '')
print(" = ", end = '')
print(sum)
