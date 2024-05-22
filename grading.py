
score = int(input("Enter the score: "))


if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 40:
    grade = "D"
else:
    grade = "E (Fail)"


print(f"The student's grade is: {grade}")
if score <= 39:
    print("The student is required to take a supplementary examination.")