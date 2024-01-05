#Conditionals

my_condition = False

if my_condition:
    print("The condition is True")

print("This is outside the if statement")

number = 5 * 7

if number>10 and number <20:
    print("The number is greater than 10 and less than 20 ")
elif number == 35:
    print("The number is 35")
else:
    print("The number isn't between 10 and 20 and also is different than 35")

#Empty string is False
my_string = ""

if not my_string:
    print("The string is empty")

