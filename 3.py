# Ejercicio 5
# Constantes
A = ["", "a", "b"]
B = ["", "b"]
C = ["ad", "bd"]

# A(B ∩ C) => d = B ∩ C 
d = set(B) & set(C)
d = list(d)

# El tamaño de la concatenacion de A(d) es la multiplicacion
# de la longitud de A por la longitud de d. Como es 0 no se
# puede realizar la concatenacion
n = len(A) * len(d)

print(d)
print(n)
