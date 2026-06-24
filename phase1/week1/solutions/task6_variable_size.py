"""Task 6 (optional) — Look at where a variable lives (practices Q7).

Goal: set x = 5, then print id(x) (an identifier tied to its place in
memory) and sys.getsizeof(x) (its size in bytes). Repeat for a huge integer
and a string, and notice how the byte counts change.

This task is optional — a stretch for when you want to go further.
"""

# Q7: Dónde vive una variable mientras el programa se ejecuta? R/ RAM

import sys                                    #solicitar herraientas del múdulo sys, time, os, math, random, urllib.request.

x = 5                                         #small integer

print("     Small Integer    ")
print(f"Value: {x}")
print(f"Memory ID: {id(x)}")                   # id() muestra un identificador asociado al objeto en la memoria
print(f"Size: {sys.getsizeof(x)} bytes")       # getsizerof() muestra cuántos bytes ocupa 
#sys.getsizeof(x)  cuánto espacio en la RAM está usando este objeto?

big_number = 999999999999999999999999999999   # Large integer

print("     Large Integer    ")
print(f"Value: {big_number}")
print(f"Memory ID: {id(big_number)}")
print(f"Size: {sys.getsizeof(big_number)} bytes")

# String

text = "Hello, Python"

print("    String    ")
print(f"Value: {text}")
print(f"Memory ID: {id(text)}")
print(f"Size: {sys.getsizeof(text)} bytes")


#el string ocupa más memoria que el large integer y el small integer







#import...
"""Módulo	                 ¿Para qué sirve?
time	                  Medir tiempo, pausas
urllib.request	          Hacer solicitudes web
os	                      Trabajar con archivos y carpetas
sys                    	  Interactuar con Python y el sistema
math	                  Funciones matemáticas
random	                  Números aleatorios"""