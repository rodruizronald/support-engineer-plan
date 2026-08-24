"""Task 1 — The same file, text and bytes (practices Q6).

Goal: write a short string containing a non-ASCII character ("café\\n") to a
file in text mode with encoding="utf-8". Then read that same file back twice
— once in text mode ("r") and once in binary ("rb") — printing both results
and the len() of each. Watch Week 2's str-vs-bytes distinction reappear, now
coming through open().
"""

#guardamos el texto uqe queremos escribir en el archivo
text = "café\n"

# abrimos el archivo en modo texto y lo escribimos usando UTF-8
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write(text)


#leemos el mismo archivo, pero en modo texto
with open("sample.txt", "r", encoding="utf-8") as file:
    text_data = file.read()


#leemos el mismo archivo, pero ahora en modo binario
with open("sample.txt", "rb") as file:
    binary_data = file.read()


#resultados: mostramos el contenido, el tipo y la longitud de cada lectura
print("--- TEXT MODE ---")
print("Result:", repr(text_data))
print("Type:", type(text_data))
print("Length:", len(text_data))

print("\n--- BINARY MODE ---")
print("Result:", binary_data)
print("Type:", type(binary_data))
print("Length:", len(binary_data))
