#Sets
#A set is a collection of items that is unordered, unchangeable, and unindexed.
#Sets are written with curly brackets, and they have no special meaning to Python.
#Sets are mutable, meaning that we can add or remove items from them.
# The sets doesn't accept duplicates.

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #initially it is a dictionary

my_other_set = {"Said", "Valencia", 28}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("said-codes")
#a set is unordered
print(my_other_set)

#a set does not allow duplicates
my_other_set.add("said-codes")
print(my_other_set)

my_other_set.remove("said-codes")

print("Said" in my_other_set)
print("Sai" in my_other_set)

my_other_set.remove("Said")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

#del my_other_set # it deletes the set
my_set = {"Said", "Valencia", "said-codes", 28}
my_other_set = {"Kotlin", "Ruby", "Python", "JavaScript"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"Java"}))
print(my_other_set.difference(my_set))
