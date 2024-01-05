# Error types

# SyntaxError
#print "Hello world"
print("Hello world")

# NameError
#language = "spanish"
#print(language)

# IndexError
my_list = ["Python", "Java"]
#print(my_list[2])


#ModuleNotFoundError
#import maths
#print(maths.pi)

# AttributeError
import math
#print(math.PI)


# KeyError
my_dict = {"name": "John", "age": 30}
#print(my_dict['lastname'])

# TypeError
my_list = ["Python", "Java"]
#print(my_list["lastname"])


# ImportError
#from math import PI
#print(PI)

from math import pi as PI_VALUE
print(PI_VALUE)

# ValueError
print(int("hello world"))

# ZeroDivisionError
#print(10/0)
