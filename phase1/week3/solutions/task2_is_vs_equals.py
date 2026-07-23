"""Task 2 — `is` vs `==` (practices Q3).

Goal: make two lists with identical contents and show that == is True but is
is False. Then show integer interning: a = 256; b = 256; print(a is b)
(usually True) versus a = 257; b = 257; print(a is b) (often False). Let this
convince you to compare values with == and reserve `is` for None.
"""

#Comparar 2 listas

list1 = [1, 2, 3]
list2 = [1, 2, 3]                        # 2 lista con el mismo contenido

print("    Comparing Lists")

print("list1 == list2:", list1 == list2)      #compara los valores
print("list1 is list2:", list1 is list2)      #compara si son el mismo objeto

print()

print("id(list1):", id(list1))
print("id(list2):", id(list2))

print()

# (enteros pequenios son reutilizados por Python)

a = 256                                  #entero pequeno
b = 256                                  #Python casi siempre reutiliza el mismo objeto

print("    Integer Interning (256)")
print("a == b:", a == b)
print("a is b:", a is b)

print()

a = 257
b = 257

print("    Integer Interning (257)")
print("a == b:", a == b)
print("a is b:", a is b)

print()

print("    Recommendation")
print("Use == to compare values.")
print("Use 'is' only to compare with None.")
