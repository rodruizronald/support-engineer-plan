"""Task 4 — Metadata is not contents (practices Q3).

Goal: take the file from Task 1 and print its .stat() fields: st_size in
bytes, st_mtime formatted as a real date with datetime.fromtimestamp(), and
the permission bits as oct(st.st_mode)[-3:]. Then append one line to the file
and print the size and modification time again to watch both change.
"""


from pathlib import Path
from datetime import datetime


#creamos la ruta al archivo que usamos en Task 1
file_path = Path(__file__).parent / "sample.txt"


#obtenemos los metadatos del archivo antes de modificarlo
st = file_path.stat()

print("--- BEFORE APPENDING ---")

print("Size:", st.st_size, "bytes")  # este es el tamaño del archivo en bytes
print(
    "Last modification:",
    datetime.fromtimestamp(st.st_mtime)
)  #convierte  el timestamp a una fecha legible 
print(
    "Permission bits:",
    oct(st.st_mode)[-3:]
)  #se muestran los últimos tres dígitos de los permisos


#agregamos una nueva línea al final del archivo
with open(file_path, "a", encoding="utf-8") as file:
    file.write("New line\n")


#obtenemos nuevamente los metadatos después de que modifiquemos el archivo
st = file_path.stat()

print("\n--- AFTER APPENDING ---")

print("Size:", st.st_size, "bytes")
print(
    "Last modification:",
    datetime.fromtimestamp(st.st_mtime)
)
print(
    "Permission bits:",
    oct(st.st_mode)[-3:]
)