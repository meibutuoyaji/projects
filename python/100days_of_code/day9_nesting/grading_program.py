student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for grades in student_scores:
    score = student_scores[grades]
    if score > 90:
        student_grades[grades] = "Outstanding"
    elif score > 80:
        student_grades[grades] = "Exceeds Expectations"
    elif score > 70:
        student_grades[grades] = "Acceptable"
    else:
        student_grades[grades] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)
