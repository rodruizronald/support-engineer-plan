"""Task 4 — Catch a signal (practices Q8).

Goal: register a handler for SIGINT (Ctrl-C) with signal.signal(), then loop
forever printing a heartbeat. When you press Ctrl-C, instead of dying
instantly the handler runs, prints a "shutting down gracefully..." message,
and exits cleanly. This is the difference between SIGINT/SIGTERM (catchable)
and SIGKILL (not).
"""


import signal
import sys
import time


#esta función se ejecuta cuando se recibe la señal SIGINT (Ctrl-C)
def handle_sigint(signum, frame):
    print("\nShutting down gracefully...")
    sys.exit(0)


#registramos la función handle_sigint como manejador de la señal SIGINT
signal.signal(signal.SIGINT, handle_sigint)

print("Program is running. Press Ctrl-C to stop.")


#loop infinito que imprime un "latido" cada segundo
while True:
    print("Heartbeat...")
    time.sleep(1)