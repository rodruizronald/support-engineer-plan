"""Task 3 — Break an encoding, then fix it (practices Q6 and Q7).

Goal: take a string with a non-ASCII character ("café" or "naïve 😀"),
.encode() it as UTF-8, then deliberately try to .decode() those bytes as
ASCII and catch the UnicodeDecodeError. Then decode them correctly as UTF-8.
Watch mojibake happen and then get fixed.
"""

# TODO: implement this task.
# Original text

text = "café"                               # Texto con un carácter que NO pertenece a ASCII

# Convert the text into bytes

encoded_text = text.encode("utf-8")         # Convierte el texto a bytes usando "utf-8"

print(" Original text ")
print(text)

print()

print("  UTF-8 bytes ")
print(encoded_text)                               # Muestra cómo se almacenan esos bytes

print()

# Try to decode using the wrong encoding

print(" ---Trying ASCII ---")

try:
    wrong_text = encoded_text.decode("ascii")       # Intenta leer los bytes como ASCII (aquí fallará)
    print(wrong_text) 

except UnicodeDecodeError as error:                 # Captura el error sin que se detenga el programa
    print("Error:", error)

print("-" * 90)

# Decode using the correct encoding

correct_text = encoded_text.decode("utf-8")          # Lee los bytes usando la codificación correcta

print(" Decoding with UTF-8 ")
print(correct_text)

print()

# Mojibake

print(" Mojibake example ")

mojibake = "cafÃ©"                              # Así suele verse cuando UTF-8 se interpreta incorrectamente
print(mojibake)

print()

print(" Correct text ")
print(text)
