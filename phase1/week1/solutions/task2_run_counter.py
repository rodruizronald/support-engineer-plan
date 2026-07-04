"""Task 2 — Survive a reboot (practices Q8).

Goal: remember how many times this script has been run. On the first run,
write 1 to a file. On every later run, read the number, add one, and write
it back — so the count survives after you close everything or reboot.
"""


filename = "counter.txt"                           #el nombre del archivo donde guardamos el conteo

try:                                               #intenta abrir el archivo para leer el conteo
    with open(filename, "r") as file:              #abre el archivo, úsalo y ciérralo automáticamente
        count = int(file.read()) 


except FileNotFoundError:
    count =0                                       #si el archivo no existe, empieza el conteo en 0

count += 1                                         #este valor se guarda en RAM, no en el disco


with open (filename, "w") as file:                 #abre el archivo para escribir el conteo, lo crea si no existe
    file.write(str(count))                         #escribe el conteo actualizado en el archivo (es decir, se guarda en el disco)


    print (f"This script has been run {count} times." )        #f"...{variable}"   es para imrpimir la variable que va entre {}
