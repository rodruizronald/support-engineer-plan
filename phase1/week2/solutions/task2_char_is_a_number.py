"""Task 2 — A letter is a number is a byte (practices Q4).

Goal: take the character "A", get its code point with ord(), turn a number
back into a character with chr(), then .encode() a short string to bytes and
print the raw byte values. See for yourself that "A" is 65 is 0x41.
"""

letter = "A"                         
code_point = ord(letter)              # Convierte la letra en su número Unicode



print(" Character to number ")
print(f"Character: {letter}")
print(f"Code point: {code_point}")    # A = 65

print()




number = 65                        
character = chr(number)               # Convierte el número nuevamente en una letra

print(" Number to character ")
print(f"Number: {number}")
print(f"Character: {character}")

print()

# Encode a string into bytes

text = "Hello"                         # Este es el texto que queremos convertir a bytes
encoded_text = text.encode("utf-8")   # Convierte el texto en bytes usando UTF-8

print(" Text to bytes ")
print(f"Original text: {text}")
print(f"Bytes: {encoded_text}")

print()





print("--- Raw byte values ---")

for byte in encoded_text:             # Recorre cada byte del texto
    print(byte)                       # Imprime el valor decimal de cada byte

print()

# Show the relationship between decimal and hexadecimal

print("--- 'A' in different forms ---")
print(f"Character : {letter}")        # La letra original
print(f"Decimal   : {code_point}")    # Su valor decimal
print(f"Hex       : {hex(code_point)}")  # Su valor hexadecimal (0x41)