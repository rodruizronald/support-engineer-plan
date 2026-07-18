"""Task 6 — Watch references rise and fall (optional — practices Q5 and Q9).

Goal: create an object, print sys.getrefcount(obj), then add it to a list and
print the count again (it goes up); del the list and watch it drop. As a
bonus, use weakref.finalize(obj, print, "collected!") to see the exact moment
the object is freed when the last reference goes away, and print
sys.getsizeof() of a small int, a huge int, and a list to tie the object
header back to Week 2's byte sizes.
"""

import sys                                                                 #para referencias y tamaños de objetos
import weakref                                                             #permite observar cuándo se elimina un obj 


class Example: 
    pass 

print ("   Reference Detective")

obj = Example()
print(f"Reference count for obj: {sys.getrefcount(obj)}")

container = [obj]
print(f"After adding to list: {sys.getrefcount(obj)}")
del container
print(f"After deleting list: {sys.getrefcount(obj)}")   

print () 

print("    Object Finalization")
finalizer = weakref.finalize(obj, print, "collected!")                       #se ejecuta cuando se elimina el objeto
print("Object still exists.")
del obj                                                                      #eliminamos la referencia al objeto
print("Object deleted") 
print()

print ("    Object Sizes")
small_int = 5
huge_int = 10**100
numbers = [1, 2, 3,]


print("Small int size:", sys.getsizeof(small_int), "bytes")
print("Huge int size:", sys.getsizeof(huge_int), "bytes")                   #entero muy grande (ocupa más bytes)
print("List size:", sys.getsizeof(numbers), "bytes")
