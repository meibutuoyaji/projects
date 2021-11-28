
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


#sum of true for name1
name1_lower_case = name1.lower()

count_t = name1_lower_case.count("t")
count_r = name1_lower_case.count("r")
count_u = name1_lower_case.count("u")
count_e = name1_lower_case.count("e")

true_1 = count_t + count_r + count_u + count_e

#sum of true for name2
name2_lower_case = name2.lower()

count_t = name2_lower_case.count("t")
count_r = name2_lower_case.count("r")
count_u = name2_lower_case.count("u")
count_e = name2_lower_case.count("e")

true_2 = count_t + count_r + count_u + count_e

#sum of true

total_true = true_1 + true_2

#sum of love for name1
name1_lower_case = name1.lower()

count_l = name1_lower_case.count("l")
count_o = name1_lower_case.count("o")
count_v = name1_lower_case.count("v")
count_e = name1_lower_case.count("e")

love_1 = count_l + count_o + count_v + count_e

#sum of love for name2
name2_lower_case = name2.lower()

count_l = name2_lower_case.count("l")
count_o = name2_lower_case.count("o")
count_v = name2_lower_case.count("v")
count_e = name2_lower_case.count("e")

love_2 = count_l + count_o + count_v + count_e


#sum of love

total_love = love_1 + love_2

#Love score

love_score = str(total_true) + str(total_love)

#convert to int

love_score_int = int(love_score)

#condition
if  (love_score_int <10) or (love_score_int >90):
    print("Your score is " + str(love_score), + "you go together like coke and mentos.")
    if (love_score_int <50) and (love_score_int >40):
        print("Your score is " + str(love_score), + "you are alright together.")
else:
    print("Your score is " + str(love_score))
