# -------------------------------------
#        Grade Checker
# -------------------------------------

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: Excellent")
elif marks >= 75:
    print("Grade: Very Good")
elif marks >= 60:
    print("Grade: Good")
elif marks >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")