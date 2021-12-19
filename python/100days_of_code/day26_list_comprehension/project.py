import pandas

data = pandas.read_csv("a.csv")

# create a dictionary in a particular format
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# create a list of the phonetic code words from a word that the user inputs.
user_name = input("What is your name?").upper()
result = [data_dict[letter] for letter in user_name]
print(result)
