### Strings ###

my_string = "My string"
my_other_string = 'My other string'
my_new_line_string = "This is a string\nwith new line"
my_tab_string = "\t This is a string with tab"
my_escaped_string = "This is a string with \"quotes\""

print(len(my_string))
print(len(my_other_string))
print(my_string, my_other_string)
print(my_string + " and " + my_other_string)
print(my_new_line_string)
print(my_tab_string)
print(my_escaped_string)

# Format Strings
name, surname, age, is_developer= "Said", "Valencia", 28, True
print("My name is  {} {}, I'm {} years old and I'm a developer: {}".format(name,surname,age,is_developer))
print("My name is  %s %s, I'm %d years old and I'm a developer: %s" %(name,surname,age,is_developer))
print(f"My name is {name} {surname}, I'm {age} years old and I'm a developer: {is_developer}")

#Character unboxing
language = "python"
a, b, c, d, e, f = language
print(a,b,c,d,e,f)

# Division or Slicing
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:5:2]
print(language_slice)


# Reverse
reversed_language = language[::-1]
print(reversed_language)

# System functions
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.find("t")) # return the index od the first occurence
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith("py"))

print("Py" < "py") # The capital letters are before the lowercase letters
