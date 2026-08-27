"""Task 5 — Build a pipe, and split the streams (practices Q5).

Goal: two parts.

  (a) Recreate `cmd1 | cmd2` in Python: start a first child with
  subprocess.Popen([...], stdout=subprocess.PIPE), pass its .stdout as the
  second child's stdin=, and read the final result. Use short `python -c`
  commands on both ends so it behaves the same on every OS.

  (b) Write one line to sys.stdout and one to sys.stderr from this script,
  then run it redirecting only stdout:

      python task5_pipe_and_streams.py > out.txt

  and watch the error line stay on your screen while the normal line lands in
  the file.
"""

import subprocess
import sys


print("--- PART A: PIPE BETWEEN TWO CHILD PROCESSES ---")

# primer child:
# imprime varias líneas a stdout.

first_child = subprocess.Popen(
    [
        sys.executable,
        "-c",
        'print("INFO: started"); print("ERROR: something failed"); print("INFO: finished")'
    ],
    stdout=subprocess.PIPE,
    text=True
)


# Second child:
# lee de stdin y filtra solo las líneas que contienen "ERROR".  
second_child = subprocess.Popen(
    [
        sys.executable,
        "-c",
        'import sys; [print(line, end="") for line in sys.stdin if "ERROR" in line]'
    ],
    stdin=first_child.stdout,
    stdout=subprocess.PIPE,
    text=True
)


# el primer child ya no necesita su stdout, así que lo cerramos para que el segundo child pueda recibir EOF.
first_child.stdout.close()


#leer la salida final del segundo child.
final_output, _ = second_child.communicate()


#esperar a que el primer child termine para evitar zombies.
first_child.wait()


print("Final result from the pipe:")
print(final_output)


print("--- PART B: STDOUT VS STDERR ---")

print("This is a normal stdout line.")
print("This is an error stderr line.", file=sys.stderr)