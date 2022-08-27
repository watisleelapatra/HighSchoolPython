# Ex08-input_triangle.py
# calculate area of triangle from length of 3 sides
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area = ", end = '')
print(area)

