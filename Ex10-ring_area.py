#Ring area calculation
r1 = float(input("Enter r1: "))  #small circle
r2 = float(input("Enter r2: "))  #big circle
Pi = 22/7
Ring = Pi*(r2**2-r1**2)
print("Ring area = " + str(Ring))
