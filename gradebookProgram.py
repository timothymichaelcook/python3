#LEARNING LISTS, THIS PROGRAM CREATES A GRADEBOOK FROM A LIST OF CLASSES AND A LIST OF GRADES

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97,85, 88]


subjects.append("computer science")
grades.append(100)


gradebook = zip(subjects, grades)

gradebook = list(gradebook)

gradebook.append(("visual arts", 93))

#print(gradebook)

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)