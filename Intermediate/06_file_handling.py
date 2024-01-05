# File handling

import os
import json
import csv
import xml

"""
# .txt file
text_file = open("Intermediate/my_file.txt","r+") # w+ to create and write the text
text_file.write("\nMi nombre es Brais\nMi apellido es Moure \n35 años\nY mi lenguaje preferido es Python\nAunque también me gusta KotlinY Swift")

print(text_file.read())
print(text_file.read(10))
print(text_file.readline())
print(text_file.readline())
print(text_file.readlines())

text_file.write("\n This is a new line")
print(text_file.readline())

text_file.close()
os.remove("Intermediate/my_file.txt")
for line in text_file.readlines():
    print(line)
"""

# .json file
"""
json_file = open("Intermediate/my_file.json","w+")
json_test = {
        "name": "Brais",
        "surname": "Moure",
        "age": 35,
        "language": "Python"
}

json.dump(json_test,json_file, indent=2)

json_file.close()

with open("Intermediate/my_file.json") as json_file:
    for line in json_file.readlines():
        print(line)

json_dic = json.load(open("Intermediate/my_file.json"))
print(json_dic)
print(type(json_dic))

"""

# .csv file
"""
csv_file = open("Intermediate/my_file.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language"])
csv_writer.writerow(["Brais","Moure",35,"Python"])
csv_writer.writerow(["Juan","Perez",30,"Kotlin"])
csv_file.close()

with open("Intermediate/my_file.csv") as csv_file:
    for line in csv_file.readlines():
        print(line)
"""
"""
# .xml file
xml_file = open("Intermediate/my_file.xml","w+")
xml_writer = xml.writer(xml_file)
xml_writer.writerow(["name","surname","age","language"])
xml_writer.writerow(["Brais","Moure",35,"Python"])
xml_writer.writerow(["Juan","Perez",30,"Kotlin"])
xml_file.close()
with open("Intermediate/my_file.xml") as xml_file:
    for line in xml_file.readlines():
        print(line)
"""
