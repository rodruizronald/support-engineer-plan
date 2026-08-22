"""Task 3 — Read a big file two ways and watch memory (practices Q7).

Goal: write a file with ~200,000 numbered lines. Then count its lines twice:
once with f.read().splitlines() (whole file into RAM) and once with
for line in f: (one line at a time). Wrap each with tracemalloc.start() /
tracemalloc.get_traced_memory() and time.perf_counter(), and print the peak
memory and time for both. Same answer, wildly different footprint — expect a
difference of a few hundred times over.

Two things to look for, because both are lessons rather than bugs:

  - The streaming version may well be SLOWER in wall-clock time even though
    it uses a fraction of the memory. That trade is the point: it's what lets
    the same code survive a file bigger than your RAM.

  - The .read() version's peak memory comes out several times larger than the
    file itself, because splitlines() hands you 200,000 separate str objects,
    each carrying Week 3's object overhead.
"""

import time                                       # Para:  -medir cuánto tarda cada método
import tracemalloc                                       # -medir cuánta memoria usa Python
from pathlib import Path                                 # -trabajar con rutas de archivos


# Creamos la ruta del archivo junto al script
file_path = Path(__file__).parent / "big_file.txt"


# Creamos un archivo grande con 200,000 líneas
with open(file_path, "w", encoding="utf-8") as file:
    for number in range(200000):
        file.write(f"Line {number}\n")       #escribe una línea numerada en el archivo


print("--- WHOLE FILE READ ---")

tracemalloc.start()                          #empieza a medir memoria
start = time.perf_counter()                 

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.read().splitlines()         #lee todo el archivo y crea una lista de líneas

line_count_whole = len(lines)               

end = time.perf_counter()                 
current, peak_whole = tracemalloc.get_traced_memory()  #obtiene memoria actual y pico máximo
tracemalloc.stop()                           # deja de medir memoria

whole_time = end - start                     #calcula cuánto tardó

print("Line count:", line_count_whole)
print(f"Time: {whole_time:.6f} seconds")
print(f"Peak memory: {peak_whole / (1024 ** 2):.2f} MiB")


print("\n--- STREAMING READ ---")

tracemalloc.start()                          # acá mpieza una nueva medición de memoria
start = time.perf_counter()                 

line_count_stream = 0                        

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:                        #lee una sola línea a la vez
        line_count_stream += 1               #suma 1 por cada línea encontrada

end = time.perf_counter()                 
current, peak_stream = tracemalloc.get_traced_memory()  #obtiene el pico de memoria
tracemalloc.stop()                           #deja de medir la memoria

stream_time = end - start                    #ahora calculamos cuánto tardó la lectura en streaming

print("Line count:", line_count_stream)
print(f"Time: {stream_time:.6f} seconds")
print(f"Peak memory: {peak_stream / (1024 ** 2):.2f} MiB")