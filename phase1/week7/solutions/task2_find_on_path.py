"""Task 2 — Find a program the way the shell does (practices Q2).

Goal: split os.environ["PATH"] on os.pathsep and print each directory on its
own line — the exact list the shell searches, in order. Then use
shutil.which() to resolve a few command names ("python3", "git",
"definitely-not-a-real-command") and print where each was found, or that it
wasn't found at all. You've just reimplemented `which`.
"""


import os
import shutil


#obtener el contenido de la variable PATH
path_value = os.environ["PATH"]

#separar PATH en cada directory individual
path_directories = path_value.split(os.pathsep)


print("--- DIRECTORIES IN PATH ----")

# mostrar cada directory en el orden en que aparece en PATH
for directory in path_directories:
    print(directory)


print("\n--- COMMAND SEARCH ---")

#comandos que queremos buscar
commands = [
    "python3",
    "git",
    "definitely-not-a-real-command"
]


# buscar cada comando usando PATH
for command in commands:
    location = shutil.which(command)

    if location:
        print(f"{command}: {location}")
    else:
        print(f"{command}: not found")