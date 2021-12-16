a = [["sato", "suzuki"], ["taka", "kouda"]]

print(a[1])
print(a[0][1])
print(a[1][1])

age = 0

if age >= 20:
    print("adult")
elif age == 0:
    print("baby")
else:
    print("child")

# for variable in range (how many times to repeat):

# for i in range(5):
#     print(i)

#break

for i in range(5):
    if i == 4:
        break
    print(1)

#nest
for i in range(3):
    for j in range(3):
        print(i, j, sep="-")

arr = [1, 2, 4, 3, 2]
sum = 0
for i in arr:
    sum += i
print(sum)


# function
def say_hello(greeting):
    print(greeting)


say_hello("test")

#class


class Student:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def avg(self, math, english):
        print((math + english) / 2)


a001 = Student("taka")
print(a001.name)

a002 = Student("tak")
print(a002.name)
