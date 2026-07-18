"""Task 5 — Shallow copy vs deep copy (practices Q6).

Goal: take a nested list like original = [[1, 2], [3, 4]], make a shallow
copy (copy.copy(original) or original[:]), then run original[0].append(99)
and watch the change bleed into the "copy." Now do the same with
copy.deepcopy(original) and show it stays isolated — shallow copy only
protects the top level.
"""

import copy                                               # importamos el módulo para hacer copias
# Lista original anidada 

original = [[1, 2], [3, 4]]                               #lista que contiene otras listas



"""Hacemos una copia superficial (shallow copy) de la lista orginal. Esta copia solo copia la lista principal,
pero no las listas internas. Por eso, si modificamos una lista interna de la original,
también se verá reflejado en la copia superficial.
Shallow copy """



shallow = copy.copy(original)                              #se copia solo la lista principal

print("   Shallow Copy")

print("Original:", original)
print("Shallow:", shallow)

print()

print("Original id:", id(original))                         #Lista principal
print("Shallow id:", id(shallow))                           # Lista proncipal nueva 

print("Original[0] id:", id(original[0]))                   # 1era lista interna
print("Shallow[0] id:", id(shallow[0]))                     # (misma lista interna)

print()

original[0].append(99)                                      # acá modifica la lista interna

print("After modifying original")

print("Original:", original)
print("Shallow:", shallow)

print()



#Deep copy



original = [[1, 2], [3, 4]]                               # reiniciamos la lista original

deep = copy.deepcopy(original)              
print("   Deep Copy")

print("Original:", original)
print("Deep:", deep)

print()

print("Original[0] id:", id(original[0]))                 # lista interna del original
print("Deep[0] id:", id(deep[0]))                         #lista interna diferente

print()

original[0].append(99)            # acá modifica la lista interna del original, pero no afecta a la deep copy 

print("After modifying original")

print("Original:", original)
print("Deep:", deep)