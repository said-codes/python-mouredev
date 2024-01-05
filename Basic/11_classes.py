#Classes
#The classes in python are blueprints for creating objects.

class MyEmptyClass:
    pass

class Person:
    def __init__(self,name, surname, age, alias = "No alias"):
        self.__name = name # private attribute
        self.__surname = surname
        self.__age = age
        self.__alias = alias

    def __str__(self):
        return f"{self.__name} {self.__surname} is {self.__age} years old, aka: ({self.__alias})"

    def walk(self):
        print(f"{self.__name} is walking")

    def get_alias(self):
        return self.__alias

    def set_alias(self, alias):
        self.__alias = alias


my_person = Person("Said", "Valencia", 28)
print(my_person)
my_person.walk()

my_other_person = Person("John", "Doe", 30, "jhondev")
print(my_other_person)

my_person.set_alias("saidcodes")
print(my_person)



