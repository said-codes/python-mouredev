# Regular expressions

import re

my_string="This is the lesson number seven: the Lesson regular expressions"
my_other_string="This is not the lesson number eight: regular expressions"

match = re.match("This is the lesson", my_string, re.I)
my_other_match =re.match("This is the lesson", my_other_string)

print(match.span())
start, end = match.span()
print(my_string[start:end])

if not(my_other_match == None):
    print(my_other_match.span())
    start, end = my_other_match.span()
    print(my_other_string[start:end])
else:
    print("No match")

# search

search = re.search("lesson", my_string, re.I)
print(search.span())

# findall

findall = re.findall("lesson", my_string, re.I)
print(findall)

# split

split = re.split(":", my_string)
print(split)

# sub

sub = re.sub("[L|l]esson", "lesson", my_string, re.I)
print(sub)

# Patterns

pattern = r'[lL]esson'
print(re.findall(pattern, my_string))

pattern = r'[lL]esson|expressions'
print(re.findall(pattern,my_string))

pattern = r'a-z'
print(re.findall(pattern, my_string))

pattern = r'0-9'
print(re.findall(pattern,my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern,my_string))

pattern = r'[l].*'
print(re.findall(pattern,my_string))

# email validation regular expressions
def validate_email(email):
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(pattern, email):
        return True
    return False

email = "said@gmail.com"
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'

print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))
