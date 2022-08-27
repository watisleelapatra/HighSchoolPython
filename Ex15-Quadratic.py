#Quadratic equation solver
a = float(input("Enter coefficient a : "))
b = float(input("Enter coefficient b : "))
c = float(input("Enter coefficient c : "))
d = (b**2 - 4*a*c)
if d < 0 :
    d = -d
    print("x1 = ", end='')
    print(-b/(2*a), end='')
    print(" + ", end='')
    print(d**0.5/(2*a),end='')
    print("i")
    print("x2 = ", end='')
    print(-b/(2*a), end='')
    print(" - ", end='')
    print(d**0.5/(2*a),end='')
    print("i")
else :
    print("x1 = ", end='')
    print((-b+(d)**0.5)/(2*a))
    print("x2 = ", end='')
    print((-b-(d)**0.5)/(2*a))
    

    
