"""Task 6 — Buffering, flushing, and an atomic write (optional — practices
Q4 and Q9).

Goal: two parts.

  (a) Open a file for writing, write a line without closing it, and
  immediately try to read the file from a second handle — see nothing there
  yet; then call .flush() and read again to watch it appear.

  (b) Do a safe write: write the new contents to config.tmp, then
  os.replace("config.tmp", "config.json") to swap it into place in one atomic
  step, so a reader can never catch a half-written file.

This task is optional — a stretch for when you want to go further.
"""

import os
from pathlib import Path


#creamos rutas dentro de la misma carpeta del script
script_directory = Path(__file__).parent
buffer_file = script_directory / "buffer_test.txt"
temp_file = script_directory / "config.tmp"
config_file = script_directory / "config.json"


print("--- PART A: BUFFERING AND FLUSHING ---")

#abrimos el archivo para escribir, pero todavía no lo cerramos para que el contenido pueda quedarse en el buffer de Python
writer = open(buffer_file, "w", encoding="utf-8")

#escribimos una línea; puede quedarse temporalmente en el buffer de Python
writer.write("Hello from the buffer!\n")

#abrimos el mismo archivo otra vez desde otro handle para leerlo
with open(buffer_file, "r", encoding="utf-8") as reader:
    before_flush = reader.read()

print("Before flush:", repr(before_flush))

# forzamos a Python a enviar su buffer al sistema operativo
writer.flush()


with open(buffer_file, "r", encoding="utf-8") as reader:  #volvemos a leer el archivo desde otro handle
    after_flush = reader.read()

print("After flush:", repr(after_flush))

writer.close() #para cerrar el archivo y liberar recursos


print("\n--- PART B: ATOMIC WRITE ---")

#escribimos primero el contenido nuevo en un archivo temporal
with open(temp_file, "w", encoding="utf-8") as file:
    file.write('{"status": "updated"}\n')

#aquí reemplazamos el archivo final en un solo paso
os.replace(temp_file, config_file)

print("Atomic replace completed.")

# por último leemos el archivo final para comprobar el resultado
with open(config_file, "r", encoding="utf-8") as file:
    print("Final config:", file.read())