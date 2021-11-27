
age = input("What is your current age?")


age_int = int(age)

years_age = 90 - age_int
months_age = years_age * 12
weeks_age = years_age * 52
days_age = years_age * 365

print("You have " + str(days_age) + " days," + str(weeks_age) + " weeks," + " and " + str(months_age) + " months left." )
