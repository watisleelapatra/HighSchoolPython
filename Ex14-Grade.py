#grading program
score = float(input("Enter your score : "))
if score > 100 or score < 0 :
    print("score must be 0-100")
elif score < 100 and score >= 80 :
    print("you get A ")
elif score < 80 and score >= 70 :
    print("you get B ")
elif score < 70 and score >= 60 :
    print("you get C ")
elif score < 60 and score >= 50 :
    print("you get D ")
else :
    print("you get F ")
