"""Task 4 — Time a network request (practices Q10).

Goal: use urllib.request.urlopen() to fetch a public URL once and print how
long it took. Wrap it in try/except so a dropped connection doesn't crash
the script. Compare this to your memory and disk timings from Task 3.
"""


import time                                                       #import es para usar un módulo (time) que contiene herramientas                                                    
import urllib.request                                             #como pedirle "Quiero usar herramientas para comunicarme con páginas web"

try:


    start = time.perf_counter()                                   #guardar el tiempo inicial

    response = urllib.request.urlopen("https://www.python.org")   #solicitud de red

    end = time.perf_counter()

    network_time = end - start                                     #cálculo de tiempo 

    print("\n    Network Test    ")
    print(f"Network request time: {network_time:.6f} seconds")     

except Exception as error:                                         #se pone después de print

    print("Network request failed.")
    print(error)
