"""Task 4 — The mutable default argument trap (practices Q7).

Goal: write the buggy def add(item, bucket=[]): bucket.append(item); return
bucket, call it three times with different items, and watch the same list
grow across calls (print id(bucket) to prove it is literally the same list
each time). Then write the bucket=None fix and show each call now starts
fresh.
"""

# Versión con el problema de argumento por defecto mutable

def add_buggy(item, bucket=[]):                 #la lista por defecto se crea una sola vez
    bucket.append(item)                         #agregamos el elemento a esa misma lista
    print("bucket id:", id(bucket))             #se muetra que es el mismo objeto en cada llamada
    return bucket


print("    Buggy version")

print(add_buggy("apple"))                       #1era llamada
print(add_buggy("banana"))                      #2da
print(add_buggy("orange"))                      #3ra

print()

#versión corregida con None

def add_fixed(item, bucket=None):               #None no crea una lista compartida
    if bucket is None:                          #aquí se comprueba si no se recibió una lista
        bucket = []                             #se crea una lista nueva para esta llamada

    bucket.append(item)                         #agrega el elemento a la lista nueva
    print("bucket id:", id(bucket))             #el id de la lista cambia en cada llamada
    return bucket                               #devolvemos la lista neva


print("    Fixed version")

print(add_fixed("apple"))                       #empieza con una lista nueva
print(add_fixed("banana"))
print(add_fixed("orange"))


"""
Por qué falla la primera función?
Python crea la lista [] una sola vez, cuando lee y define la función.
No crea una lista nueva cada vez que llamas a la función. Por eso las tres llamadas
reutilizan exactamente la misma lista.
"""