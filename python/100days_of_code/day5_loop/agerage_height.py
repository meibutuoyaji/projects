# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#total  height
total_height = 0
for total in student_heights:
    total_height += total
#print(total_height)

#total number
total_number = 0
for number in student_heights:
    total_number += 1
#print(total_number)

#average
average = total_height / total_number
print(round(average))
