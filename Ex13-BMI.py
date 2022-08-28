# BMI calculation
w = float(input("Enter your weight in kg: "))
hcm = float(input("Enter your height in cm: "))
hm = hcm/100
bmi = w/hm**2
print("Your BMI = " + str(bmi))
if bmi < 18.5 :
    print("you are underweight")
elif bmi >= 18.5 and bmi < 24.9 :
    print("you are normal")
elif bmi >= 25 and bmi < 29.9 :
    print("you are overweight")
elif bmi >= 30 and bmi < 34.9 :
    print("you are obese")
elif bmi > 35 :
    print("you are extremely obese")

