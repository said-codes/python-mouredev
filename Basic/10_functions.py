### Functions ###
# Functions are a way to organize code that performs a specific task.

def my_function():
    print("Hello from a function")


my_function()


def sum_two_values(first_number: int, second_number: int):
    return first_number + second_number


print(sum_two_values(2, 3))

my_result = sum_two_values(89, 20)
print(my_result)


def print_name(name: str, surname: str):
    print(f"Hello {name} {surname}")


print_name(surname="Valencia", name="Said")


def print_name_with_default_value(name: str = "No name provided",
                                  surname: str = "No surname provided",
                                  alias: str = "No alias provided",
                                  *args, **kwargs):
    if len(args) == 3:
        print(f"Hello {name} {surname}, your alias is {alias}")
    else:
        print(f"Error not enough arguments: {name}, {surname}, {alias}")

    if kwargs:
        print("Keyword arguments")
        for key, value in kwargs.items():
            print(f"key: {key}, value: {value}")


print_name_with_default_value(surname="Valencia", name="Said", age=28)


def print_texts(*text):
    # print(text)
    for t in text:
        print(t)


print_texts("Hello", "World", "!")
