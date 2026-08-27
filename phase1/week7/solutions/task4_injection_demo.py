"""Task 4 — Watch a command injection happen, safely, on your own machine
(practices Q4 and Q7).

Goal: put a hostile-looking string in a variable —

    untrusted = "hello; touch INJECTED.txt"

— then pass it to a child process TWO ways, and each time print the argument
the child actually received AND check whether INJECTED.txt now exists:

  (a) as one element of a list:
      [sys.executable, "-c", "import sys; print('arg =', repr(sys.argv[1]))",
       untrusted]
      -> the child reports the WHOLE string as one literal argument,
         and no file appears.

  (b) glued into a single string with shell=True:
      -> the child reports only 'hello', and INJECTED.txt GETS CREATED.
         The shell saw the ';', cut your command in half, and ran the rest
         as a second command.

Delete the marker file when you're done.

Judge this by the FILE, not by the printed text: the word "INJECTED" appears
in both runs, because it is part of the string being echoed. The only
unambiguous proof is the side effect on disk plus the truncated argument.

On Windows, shell=True runs cmd.exe, where ';' is NOT a command separator —
use '&' in place of ';' (and `type nul > INJECTED.txt` in place of `touch`)
to see the same thing. That difference is worth noticing on its own: "which
shell am I actually handing this to?" is the question behind a lot of
cross-platform breakage.
"""

import subprocess
import sys
from pathlib import Path


# marcador de archivo para ver si el comando hostil se ejecutó
marker_file = Path("INJECTED.txt")


# eliminar el archivo marcador si ya existe, para que podamos ver si se crea de nuevo
if marker_file.exists():
    marker_file.unlink()


#Windows version:
# cmd.exe usa & como separador de comandos, no ;. Y no tiene touch, así que usamos type nul > INJECTED.txt
untrusted = "hello & type nul > INJECTED.txt"


print("--- PART A: LIST FORM ---")

result = subprocess.run(
    [
        sys.executable,
        "-c",
        "import sys; print('arg =', repr(sys.argv[1]))",
        untrusted
    ],
    capture_output=True,
    text=True
)

print("Child output:")
print(result.stdout.strip())

print("INJECTED.txt exists:", marker_file.exists())


print("\n--- PART B: shell=True ---")

command = (
    f'"{sys.executable}" -c '
    f'"import sys; print(\'arg =\', repr(sys.argv[1]))" '
    f'{untrusted}'
)

result = subprocess.run(
    command,
    shell=True,
    capture_output=True,
    text=True
)

print("Child output:")
print(result.stdout.strip())

print("INJECTED.txt exists:", marker_file.exists())


#limpiar el archivo marcador al final para que podamos volver a ejecutar este script sin problemas
if marker_file.exists():
    marker_file.unlink()

print("\nMarker file deleted.")
