"""Task 3 — Time memory against disk (practices Q2 and Q9).

Goal: measure two things with time.perf_counter() and compare them:
  1. a for loop running a few million trivial iterations (pure RAM/CPU work)
  2. reading a small text file many times in a loop (touches the disk)
Print both timings and notice how much slower touching the disk is.
"""

import time
from pathlib import Path                             #obtiene la carpeta donde está este script, ya que python no lo encontró (EXPLICAR)

sample_file = Path(__file__).parent / "sample.txt"   #ruta hacia sample.txt

start = time.perf_counter()                          #tiempo de inicio (CPU/RAM)


for i in range(5000000):                             # Repetimos 5 millones de veces.
    pass                                             #Significa "no hacer nada" (para esperar)

end = time.perf_counter()                            # Guardar el tiempo final.

cpu_time = end - start                               # Calcular cuánto tardó.


#TIEMPO DE DISCO

start = time.perf_counter() 


for i in range(1000):                                 #abrimos y leemos el archivo mil veces (obliga a python a acceder al disco)
    with open(sample_file, "r") as file:
        file.read()

end = time.perf_counter()

disk_time = end - start                                 

print("\nPerformance Results")                           # \n   sirve para salto de línea 
print("-" * 30)                                          #    "-" * 30 líneas, imprime 30 líneas como separador

print(f"CPU/RAM loop time: {cpu_time:.6f} seconds")
print(f"Disk read time: {disk_time:.6f} seconds")