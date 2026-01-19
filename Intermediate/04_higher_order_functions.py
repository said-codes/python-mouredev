# Higher order functions
from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(firstnumber, secondnumber, sum_five):
    return sum_five(firstnumber + secondnumber )

print(sum_two_values_and_one(1,2,sum_five))

# Closures
# the closure are functions that return other functions
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)

print(add_closure(5))
print((sum_ten(5))(1))

# Build-in higher order functions

numbers = [1,2,3,4,5,6,7,8,9,10,78]

def multiply_two(value):
    return value * 2

# map
print (list(map(multiply_two, numbers)))
print(list(map(lambda value: value * 2, numbers)))

def filter_greater_than_ten(value):
    if value > 10:
        return True
    return False

# filter

filtered_numbers = list(filter(filter_greater_than_ten, numbers))
print(filtered_numbers)
print(list(filter(lambda number: number > 10, numbers)))

def sum_two_values(firstnumber, secondnumber):
    return firstnumber + secondnumber

# reduce

print(reduce(sum_two_values,numbers))
