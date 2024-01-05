#Dictionaries
#Dictionaries are a data structure that allow us to store key-value pairs.
#A key-value pair is a way to associate data with a name.

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_dict = {
    "occupation": "developer",
    "name": "Said",
    "lastname": "Valencia",
    "age": 28,
    "languages": {"Python", "Ruby", "JavaScript", "Java"}
    }

my_other_dict = {2: "book", "title": "The immigrants", "author": "Howard Fast"}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_other_dict["title"])

my_dict["speaks"] = {"Spanish", "English", "French"}
print(my_dict)

del my_dict["speaks"]
print(my_dict)

print("occupation" in my_dict)
print("Said" in my_dict.values())

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("name", "lastname", "age"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
