# Lambdas
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression

sum = lambda x,y : x+y
print(sum(2,9))

multiply_values = lambda x,y,z : x*y*z

print(multiply_values(2,3,4))

def sum_values(number):
    return lambda firstvalue, secondvalue: firstvalue + secondvalue + number

print(sum_values(5)(3,9))

