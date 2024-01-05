#Loops
#The loops are used to repeat a block of code several times.

#While
number = 0
while number < 10:
    print(number)
    # number = number + 1
    number += 1
else:
    print("Number is greater than 10")


number = 0
while number < 20:
    if number == 10:
        print("Number is 10\nbreak")
        break
    elif number == 4:
        print("Number is 4\npass")
        pass
    else:
        print(number)
    number += 1

#For
#An iterable is an object that can be iterated over.
my_list = [1, 2, 3, 4, 5]
my_tuple = (28, 89, 20, 40)
my_set = {10, 21, 30, 4}
my_dict = {"name": "John", "age": 30, "city": "New York"}

for item in my_list:
    print(item)

for item in my_tuple:
    print(item)

for item in my_set:
    print(item)


for item in my_dict:
    if item == "age":
        break
    else:
        print(item)
else:
    print("The end")


for key, value in my_dict.items():
    print(key, value)
else:
    print("The end")
