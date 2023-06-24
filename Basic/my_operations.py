def sum_two_values(a, b):
    return a + b

#check that the numbers passed to the functions are integers and prints a message
def check_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        print("The numbers must be integers")
    else:
        print("The numbers are integers")
