# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparatures = []
#     for row in data:
#         if row[1] != "temp":
#             temparatures.append(int(row[1]))
#     print(temparatures)

import pandas

data = pandas.read_csv("weather_data.csv")

dictionary = data.to_dict()

temp_list = data["temp"].to_list()

# print(data["temp"].mean())
#
#
# print(data.temp)
# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"])

monday = data[data.day == "Monday"]
mon_temp = int(monday.temp)

F = (mon_temp * 9 / 5) + 32
print(F)

# num = len(temp_list)

# total = 0
# for number in temp_list:
#     total += number

# avg = round(total / num)

# print(avg)
