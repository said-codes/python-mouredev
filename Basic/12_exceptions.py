#Exceptions Handling

number_one , number_two = 8, 4
number_two = "4"

try:
    print(number_one + number_two)
except TypeError as e:
    print(f"Type error: {e}")
except Exception as e:
    #this will execute if there is an exception
    print(f"Exception error: {e}")
else:
    #this will only execute if there is no exception
    print("No exceptions")
    print("An error has not occurred")
finally:
    # this will always execute
    print("This is always executed")




