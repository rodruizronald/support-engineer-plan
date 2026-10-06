"""Task 3 — A file descriptor is just a number (practices Q7).

Goal: open a file and print its .fileno() — the integer the OS handed you.
Open two or three more without closing them and watch the numbers climb.
Then use a `with` block and confirm the descriptor is released when the block
ends. See that "open files" are literally small integers the kernel tracks.
"""

#para abrir archivos 
file1 = open("file1.txt", "w")
file2 = open("file2.txt", "w")
file3 = open("file3.txt", "w")

#se puede ver el file descriptor que corresponde a cada archivo
print("=== OPEN FILE DESCRIPTORS ===")
print("File 1 descriptor:", file1.fileno())
print("File 2 descriptor:", file2.fileno())
print("File 3 descriptor:", file3.fileno())

# Cerramos los archivos para liberar sus file descriptors
file1.close()
file2.close()
file3.close()


print("\n=== USING WITH ===")

# 'with' cierra automáticamente el archivo cuando termina el bloque
with open("with_file.txt", "w") as file:
    descriptor = file.fileno()                       
    print("Descriptor inside with block:", descriptor)
    print("Is the file closed inside the block?", file.closed)

#cuando se sale del bloque, Python cierra el archivo automáticamente
print("Is the file closed after the block?", file.closed)