"""Task 2 — Paths without string glue (practices Q8).

Goal: using pathlib.Path, build a path with the / operator, then print its
.name, .suffix, .parent, and .resolve(), and whether it .exists(). Then print
Path.cwd() next to Path(__file__).parent.

Now run this script twice — once from inside week6/solutions/, then again
from the repo root:

    python phase1/week6/solutions/task2_paths_with_pathlib.py

Watch cwd() change between the two runs while the script's own directory
stays put. That is the Q2 bug, reproduced on demand.
"""


from pathlib import Path #importamos la clase pathlib.Path para trabajar con rutas de archivos


# obtenemos la carpeta donde está guardado este script
script_directory = Path(__file__).parent

#construimos una ruta usando / en lugar d unir strings manualmente
file_path = script_directory / "sample.txt"


print(" PATH INFORMATION")

print("Name:", file_path.name) 
print("Suffix:", file_path.suffix)  # extensión del archivo
print("Parent:", file_path.parent)  # carpeta que contiene el archivo
print("Resolved path:", file_path.resolve())  # ruta absoluta
print("Exists:", file_path.exists())  # para comprobar si el archivo existe


print("\n--- WORKING DIRECTORY VS SCRIPT DIRECTORY ---")

print("Current working directory:", Path.cwd())  # desde dónde ejecutamos Python
print("Script directory:", Path(__file__).parent)  # dónde está guardado este script