"""Task 4 — Make an integer overflow on purpose (practices Q3).

Goal: Python integers never overflow, so simulate a fixed-width unsigned
8-bit counter. Start at 250, keep adding 1, and wrap every result with
% 256 (or mask it with & 0xFF). Print the value as it climbs past 255 and
snaps back to 0 — the same thing languages like C do silently.
"""

# Starting value

counter = 250                                           # Empezamos cerca del límite de un entero de 8 bits

print("--- 8-bit Unsigned Counter ---")

# Increase the counter several times

for i in range(10):                                       # Repetimos el proceso 10 veces

    print(f"Counter: {counter}")                          # Muestra el valor actual

    counter = (counter + 1) % 256                         # Suma 1 y, si llega a 256, vuelve a 0