# Variables
str_variable= "Hello String Variable"
number = 8
is_developer = True
str_number = str(number)


print(str_variable, number,is_developer)
print(f"Type of str number variable: {type(str_number)}")
print("My Boolean variable is : " , is_developer)
print(f"The length of the string is: {len('this is a str')}")
print(f"The length of the str variable is:{len(str_variable)}")

#variables in one line
name, surname, alias, age = "Said", "Valencia",  "saidcodes", 30
print("My name is : ",name, surname, "and my alias is :", alias, "and I'am", age, "years old")

# Do we force the type ?, no, we are only indicating the data type we want it to be
first_name : str = "Said"
first_name = 8
print(type(first_name))

#Inputs
first_name = input("What is your name? : ")
age = input("How old are you? :" )

print("Your name is : ", first_name, "and you are", age, "years old")
