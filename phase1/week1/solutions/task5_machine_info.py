"""Task 5 — Ask the machine about itself (practices Q1).

Goal: install psutil (`pip install psutil`) and use it plus the `platform`
module to print three of the four components as they exist on your own
machine: CPU core count, total/free RAM, and free disk space — plus the OS.
"""
#psutil se instaló desde la terminal : py -m pip install psutil
#importar librerías

import psutil                              #para preguntar sobre CPU, RAM y procesos
import platform                            #para preguntar cuál sistema operativo estoy usando
import shutil                              #funciones relacionadas con archivos y discos


# Operating System

print("Operating System")
print(platform.system())                   #mostrar el sistema operativo (Windows, Linux o Darwin)

#CPU

print("    CPU    ")
print(f"CPU cores: {psutil.cpu_count()}")  # mostrar cantidad de núcleos de la CPU 
#varios núcleos puedes realizar varios procesos a la vez, un solo núcleo, realiza una cosa a la vez


#RAM
memory = psutil.virtual_memory()                               #para obtener info de la memoria RAM

print("     RAM    ")
print(f"Total RAM: {memory.total / (1024**3):.2f} GB")         # mostrar RAM TOTAL en GB

print(f"Available RAM: {memory.available / (1024**3):.2f} GB") # mostrar RAM DISPONIBLE en GB

#Disco

disk = shutil.disk_usage("/")                                  # obtener información del disco

print("     Disk    ")
print(f"Free disk space: {disk.free / (1024**3):.2f} GB") # mostrar espacio libre del disco en GB

