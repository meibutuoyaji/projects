
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = int(weight) / (float(height) * float(height))
BMI_round = (round(BMI))

if BMI_round < 18.5:
    print("Your BMI is " + str(BMI_round) + "," + "you are underweight")
elif BMI_round < 25:
     print("Your BMI is " + str(BMI_round)  +  "," +  "you have a normal weight")
elif BMI_round < 30:
    print("Your BMI is " + str(BMI_round)  + "," +  "you are slightly overweight")
elif BMI_round < 35:
    print("Your BMI is " + str(BMI_round)  +  "," +  "you are obese")
else:
    print("Your BMI is " + str(BMI_round)  +  "," +  "you are clinically obese.")
