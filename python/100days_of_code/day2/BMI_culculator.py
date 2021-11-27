#BMI
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


BMI = int(weight) / (float(height) * float(height))
print(round(BMI))
