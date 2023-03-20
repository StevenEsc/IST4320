# Steven Escobar 10/02/2022  Give Me A Grade Ver.1
# This program will give you a grade based on your input


score = input("Please enter your score:  ")
score = int(score)

if score > 100:
    print("WOW you went above and beyond ")
elif score >= 90 and score <= 100:
    print("Congrats you have an, A")
elif score >= 80 and score <= 89:
    print("Congrats you have a, B")
elif score >= 70 and score <= 79:
    print("Congrats you have a, C")
elif score >= 60 and score <= 69:
    print("Congrats you have a, D")
elif score < 60:
    print(" F, Please retake the course ")

