import random as r

# Ejercicios 2 inciso b, ejercicio 4 y ejercicio 3 de sección 2
# Constantes
SIZE = 27
SIZE_WORD = 3
ALPHABET = ["a", "b", "c"]
ALPHABET_2 = ["a", "ab", "ac"]
SUB_WORD = "bb"
WORD = "ababbbb"

# Variables
words = []

# Definirá el limite de cadenas a formar 
def get_chains(n, type):

    # Definimos la condicion de finalizacion
    if len(words) == SIZE:

        return
    else:
        temp = get_word(SIZE_WORD - 1, type=type)

        if temp not in words:
            words.append(temp)


        return get_chains(n - 1, type=type)

# Definirá cada palabra con limite de caracteres
def get_word(n, type, word = ""):
    idx = r.randint(0, 2)

    # Definimos la condicion de finalizacion
    if n == 0:
        if type == "a":
            word += ALPHABET[idx]
        else:
            word += ALPHABET_2[idx]

        return word
    else:
        if type == "a":
            word += ALPHABET[idx]
        else:
            word += ALPHABET_2[idx]

        return get_word(n - 1, type, word)

print("Todas las posibles cadenas de 3 letras con el alfabeto dado (pregunta 4, inciso 2): ")
get_chains(SIZE - 1, "a")
print(words)

print()
words = []
print("A^3 del alfabeto dado (ejercicio 3): ")
get_chains(SIZE - 1, "b")
print(words)

print()
print("¿Es bb subcadena de ababbbb? ")
print(SUB_WORD in WORD)
