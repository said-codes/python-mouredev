# challenges

"""
  Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos y con un salto de línea entre
  cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1,101):
        if index % 3 == 0 and index % 5 ==0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5== 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()


"""
  Escribe una función que reciba dos palabras (String) y retorne
  verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagrama(word1, word2):
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

print(is_anagrama("amor", "roma"))

"""
  Escribe un programa que imprima los 50 primeros números de la sucesión
  de Fibonacci empezando en 0.
  - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0
    next = 1
    for index in range(0,50):
        print(prev)
        fib= prev + next
        prev = next
        #next = prev + next
        next = fib

fibonacci()

"""
  Escribe un programa que se encargue de comprobar si un número es o no primo.
  Hecho esto, imprime los números primos entre 1 y 100.
"""

"""
def is_prime(number):
    if number<2:
        return False
    for index in range(2,1001):
        if number % index == 0:
            return False
    return True
"""

def is_prime():
    for number in range(2, 101):
        is_divisible = False
        if number >= 2:
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)

is_prime()


"""
  Crea un programa que invierta el orden de una cadena de texto
  sin usar funciones propias del lenguaje que lo hagan de forma automática.
  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0,  text_len):
        # this is the same as: reversed_text = reversed_text + text_len[text_len - index -1]
        reversed_text += text_len[text_len - index -1]
    return reversed_text

reverse("Hello world")
