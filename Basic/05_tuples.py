#Tuples
#Tuples are immutable, so they cannot be changed
#Tuples are created using parenthesis
#Tuples are faster than lists
#Tuples are used to store multiple values in a single variable

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (28,1.80,"Said","Valencia")
my_other_tuple = (20, 24, 25, 26, 27)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) # Index error

print(my_tuple.count("Said"))
print(my_tuple.index("Valencia"))
#my_tuple[1] = 1.85 # TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:5])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[1] = 1.85
my_tuple.insert(4,"said-codes")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))

#del tuple
#print(tuple) # NameError: name 'tuple' is not defined
