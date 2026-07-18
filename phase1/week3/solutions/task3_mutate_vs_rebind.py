"""Task 3 — Mutate vs rebind (practices Q4).

Goal: try s = "cat"; s[0] = "b" and catch the TypeError — strings are
immutable. Then show that s = s + "!" gives you a new object (print id(s)
before and after — it changes), while lst = [1, 2]; lst.append(3) keeps the
same object (its id stays put). See the difference between changing a name
and changing an object.
"""

# Ejemplo con strings (inmutables)  

s = "cat"                               

print("   String Example   ")

try:
    s[0] = "b"                       # intentamos modificar la cadena (para que dé un error)

except TypeError as error:
    print("Error:", error)              

print()

# Ejemplo con strings (rebinding)

print("   Rebinding a String")

print("Before:", s)
print("id before:", id(s))              #identificador antes de que se modifique la cadena

s = s + "!"                             #aquí se crea una nueva cadena y "s" apunta a esa nueva cadena

print("After:", s)
print("id after:", id(s))               # el identificador cambia

print()

# Ejemplo con listas (mutables)

lst = [1, 2]                              #creamos una lista

print("    Mutating a List")

print("Before:", lst)
print("id before:", id(lst))            # identificador antes de que se modifique la lista

lst.append(3)                           # modificamos la lista (mutación)

print("After:", lst)
print("id after:", id(lst))             # el identificador no cambia, la lista siguie siendo la misma