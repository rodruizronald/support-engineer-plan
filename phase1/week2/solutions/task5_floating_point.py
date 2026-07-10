"""Task 5 — Prove floating point is fuzzy (practices Q8).

Goal: print 0.1 + 0.2, show it isn't 0.3, then print the result with many
decimals using f"{x:.20f}" to see the tiny error. Show the right way to
compare floats (math.isclose) and the right way to handle money
(decimal.Decimal).
"""

# TODO: implement this task.

import math                          # Permite comparar números float correctamente
from decimal import Decimal          # Permite trabajar con decimales exactos (ideal para dinero)

# Add two floating-point numbers

result = 0.1 + 0.2                   

print(" Floating-point addition ")
print(f"0.1 + 0.2 = {result}")      

print()

# Compare with 0.3

print(" Comparing with 0.3 ")
print(result == 0.3)                

print()

# Show the hidden error

print(" Showing many decimal places ")
print(f"{result:.20f}")              # Muestra 20 decimales para ver el pequeño error oculto

print()

# Correct way to compare floats

print(" Using math.isclose() ")
print(math.isclose(result, 0.3))     # Compara dos float permitiendo una pequeña diferencia

print()

# Correct way to work with money

print("--- Using Decimal ---")

money = Decimal("0.1") + Decimal("0.2")   # Suma decimal exacta

print(money)                              # Resultado exacto: 0.3