import random as r

# Ejercicio 2 inciso a
# Constantes
SIZE = 5
ALPHABET = ["a", "b", "c"]

# Variables
words = []

# Definirá el limite de cadenas a formar 
def get_chains(n):

    # Definimos la condicion de finalizacion
    if n == 0:
        temp = get_word(SIZE - 1)
        words.append(temp)

        return
    else:
        temp = get_word(SIZE - 1)
        words.append(temp)

        return get_chains(n - 1)

# Definirá cada palabra con limite de caracteres
def get_word(n, word = ""):
    idx = r.randint(0, 2)

    # Definimos la condicion de finalizacion
    if n == 0:
        word += ALPHABET[idx]

        return word
    else:
        word += ALPHABET[idx]

        return get_word(n - 1, word)


get_chains(SIZE - 1)

print("5 palabras de 5 letras cada una: ")
print(words)
