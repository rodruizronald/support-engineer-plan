"""Task 5 — Make the I/O errors happen on purpose (practices Q9).

Goal: in three small try/except blocks, trigger and catch: opening a file
that doesn't exist (FileNotFoundError), opening a directory as if it were a
file (IsADirectoryError / PermissionError), and opening an existing file with
mode "x" (FileExistsError). Print the message each one gives you. Then write
one sentence on why catching the error beats checking .exists() first.
"""



from pathlib import Path


#obtenemos la carpeta donde está este script
script_directory = Path(__file__).parent


print("--- FILE NOT FOUND ERROR ---")

try:
    #intento abrur un archivo que no existe para provocar un "FileNotFoundError"
    with open(script_directory / "does_not_exist.txt", "r", encoding="utf-8") as file:
        file.read()

except FileNotFoundError as error:
    #mostramos el mensaje de error que nos da Python
    print("FileNotFoundError:", error)


print("\n--- DIRECTORY ERROR ---")

try:
    #intentamos abrir una carpeta como si fuera un archivo
    with open(script_directory, "r") as file:
        file.read()

except (IsADirectoryError, PermissionError) as error:
    #el error puede variar dependiendo del SO y la configuración, así que capturamos ambos tipos posibles
    print(type(error).__name__ + ":", error)


print("\n--- FILE EXISTS ERROR ---")

existing_file = script_directory / "existing_file.txt"

#creamos primero el archivo para asegurarnos de que ya existe
existing_file.touch(exist_ok=True)

try:
    #el modo "x" solo permite crear un archivo si todavía no existe
    with open(existing_file, "x", encoding="utf-8") as file:
        file.write("Hello")

except FileExistsError as error:
    #capturamos el error porque el archivo ya existe :) 
    print("FileExistsError:", error)


print("\n--- WHY TRY/EXCEPT? ---")

print(
    "Catching the error is better than checking .exists() first because "
    "the file can change between the check and the open."
)