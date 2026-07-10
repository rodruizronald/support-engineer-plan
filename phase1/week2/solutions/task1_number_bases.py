"""Task 1 — See one number wear three outfits (practices Q1 and Q2).

Goal: take a number like 255 and print it in binary, decimal, and hex, then
convert back the other way. Use bin(), hex(), int("ff", 16),
int("11111111", 2), and format specs like f"{n:08b}" and f"{n:#x}". Watch a
single value look completely different in each base while staying the same
number.
"""

                                                                                
number = 255                                                                     # Este es el número que veremos en diferentes sistemas numéricos

# Mostrar el mismo número en diferentes bases
print(" Same number in different number systems ")
print(f"Decimal: {number}")                                                       # Lo muestra en base 10 (normal)
print(f"Binary: {bin(number)}")                                                   # Convierte el número a binario
print(f"Hex: {hex(number)}")                                                      # Convierte el número a hexadecimal

print()  

# Convertir desde hexadecimal a decimal
hex_number = int("ff", 16)                                                       # Lee "ff" como un número en base 16

# Convertir desde binario a decimal
binary_number = int("11111111", 2)                                               # Lee "11111111" como un número en base 2

print(" Converting back to decimal  ")
print(f"Hex 'ff' = {hex_number}")            
print(f"Binary '11111111' = {binary_number}")

print()

# Mostrar el número con (format specifiers)
print(" Using format specifiers ")
print(f"Binary (8 bits): {number:08b}")                                          # Siempre muestra 8 bits agregando ceros si hacen falta
print(f"Hex with prefix: {number:#x}")                                           # Muestra el número en hexadecimal incluyendo el prefijo 0x


