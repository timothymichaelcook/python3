#THIS PROGRAM CALCULATES LETTER GRADE BASED ON NUMERIC GRADE

print("Please enter a value from 0-100:")
grade = int(input())

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")