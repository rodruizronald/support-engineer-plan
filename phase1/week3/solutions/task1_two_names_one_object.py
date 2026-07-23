"""Task 1 — Two names, one object (practices Q1 and Q2).

Goal: write a = [1, 2, 3], then b = a, then b.append(4), and print both a
and b to see they changed together. Print id(a) and id(b) to prove they are
the same object. Then repeat with an integer (a = 5; b = a; b = b + 1) and
show that this time a is untouched — because rebinding a name is not the same
as mutating an object.
"""

a = [1, 2, 3]                        #creamos una lista
b = a                                #b apunta al mismo objeto que a

b.append(4)                          #aquí se modifica la lista

print("    List Example    ")
print("a =", a)                      #Muestra la lista de a
print("b =", b)                      # muesra la lista de b que es la misma de a

print()

print("id(a) =", id(a))              #identificador del objeto al que apunta a
print("id(b) =", id(b))              #identificador del objeto al que apunta b

print()

# Ejemplo con enteros, que son inmutables

a = 5                                #primero creamos un entero
b = a                                #b apunta al mismo entero

b = b + 1                            #b ahora "apunta" a un objeto nuevo

print("   Integer Example   ")
print("a =", a)                       # a sigue siendo 5
print("b =", b)                       # b ahora vale 6

print()

print("id(a) =", id(a))
print("id(b) =", id(b))