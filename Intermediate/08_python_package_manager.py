# Python package manager

import numpy
import pandas
import requests

print(numpy.version.version)
numpy_array = numpy.array([1,2,3,4,5,6,7,8,9,10])
print(type(numpy_array))
print(numpy_array * 2)

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=121")
print(response)
print(response.status_code)
print(response.json())

# arithmetics package
from my_package import arithmetics

print(arithmetics.sum(1,4))
