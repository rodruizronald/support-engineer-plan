"""Task 2 — Read the process table (practices Q3 and Q4).

Goal: use psutil (installed in Week 1) to loop over psutil.process_iter()
and print the PID, name, and memory of a handful of running processes — the
OS's process table, seen from Python. Then print your own process's memory
with psutil.Process().memory_info().rss.
"""

import psutil  # Importamos psutil para obtener información sobre los procesos del sistema


print("=== RUNNING PROCESSES ===")

#se recorren los procesos que se etsán ejecutando en el sistema, se obtiene su PID...
for process in list(psutil.process_iter(["pid", "name", "memory_info"]))[:10]:

    pid = process.info["pid"]  
    name = process.info["name"]
    memory = process.info["memory_info"].rss #se ve la memoriia RAM que está usando el proceso en bytes 

    memory_mb = memory / (1024 ** 2)  #se convierten los bytes en megabytes solo par que sea más legible

    print(f"PID: {pid} | Name: {name} | Memory: {memory_mb:.2f} MB")



my_process = psutil.Process()


my_memory = my_process.memory_info().rss

my_memory_mb = my_memory / (1024 ** 2)

print("\n=== MY PYTHON PROCESS ===")
print(f"My PID: {my_process.pid}")
print(f"My memory usage: {my_memory_mb:.2f} MB")