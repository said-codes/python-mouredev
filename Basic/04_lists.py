### Lists ###
# Lists are a collection of items in a particular order.
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [27, 78, 45, 12, 99, 100, 58,78]

print(my_list)
print(len(my_list))

my_other_list = [28, 1.78, "Valencia","Said"]
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(78))
#print(my_other_list[4]) # error,index out of range

# Unpacking the values in my_other_list
age, height, surname, name = my_other_list
print(age)
print(height)
print(surname)
print(name)

print(my_list + my_other_list)

# Python is a dynamically typed language, which means that we can change the type of a variable.
# my_list = "Hello Python"
# print(my_list)
# print(type(my_list))

my_other_list.append("said-codes")
print(my_other_list)

my_other_list.insert(1,"blue")
print(my_other_list)

my_other_list[len(my_other_list)-1] = "tomatoe"
print(my_other_list)

my_other_list.remove("blue")
print(my_other_list)

my_list.remove(78)
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[2:3])

