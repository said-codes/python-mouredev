### Variables ###

# convention error, to write snake case instead camel case

my_string_variable = "Hello String Variable"
my_int_variable = 8
my_bool_variable = True
my_int_to_str_variable = str(my_int_variable)

print(type(my_int_to_str_variable))
print(my_string_variable, my_int_variable,my_bool_variable)
print("My Boolean variable is : " , my_bool_variable)
#print(type(print("Hello World"))) # NoneType, because print is a function and not a variable

# system functions
print(len("this is a str"))
print(len(my_string_variable))

# Variables on a single line, beware of abusing this syntax
name, surname, alias, age= "Said", "Valencia",  "saidcodes", 28
print(name, surname, "and my alias is :", alias, "and I'am", age, "years old")

### Inputs ###

# first_name = input("What is your first name? : ")
# age = input("How old are you? :")
# print("Hello ", first_name , " you are " , age , " years old")

# Do we force the type ?, no, we are only indicating the data type we want it to be
first_name : str = "Said"
first_name = 8
print(type(first_name))


