# if-demo
Pi = 22/7
r = float(input("Enter radius: "))
if r < 0 :
    print("radius must be positive")
    r = 0
area = Pi*r**2
print("area = " + str(area))
