# List comprehension
# [expression for item in iterable]


my_original_list = [0,1,2,3,4,5,6,7]
#my_list = [i for i in my_original_list]
#my_list= [i for i in range(8)]
my_range = range(8)
#my_list= [i*i for i in range(8)]
#my_list= [i + 1 for i in range(8)]
my_list= [i*2 for i in range(8)]
print(range(8))
print(list(my_range))
print(my_list)

def sum_five(number :int):
    return number +5

my_list= [sum_five(i) for i in range(8)]
print(my_list)
