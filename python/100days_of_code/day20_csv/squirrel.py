import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_sq = data[data["Primary Fur Color"] == "Gray"]
gray_sq_count = len(gray_sq)
cinnamon_sq = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_sq_count = len(cinnamon_sq)
black_sq = data[data["Primary Fur Color"] == "Black"]
black_sq_count = len(black_sq)

print(gray_sq_count)
print(black_sq_count)
print(cinnamon_sq_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq_count, cinnamon_sq_count, black_sq_count]
}

DF = pandas.DataFrame(data_dict)
DF.to_csv("sq_count.csv")
