"""Task 6 (optional) — Spawn and reap a child process (practices Q2 and Q3).

Goal: use subprocess.Popen to launch a second process (for example
["sleep", "1"], or another short Python command). Print your own PID and the
child's .pid, call .wait() to block until it finishes, then print its
.returncode. Watch the OS create a new process and hand you back its result.

This task is optional — a stretch for when you want to go further.
"""


import os
import subprocess
import sys


#(proceso padre)
print("Parent PID:", os.getpid())


#se crea un nuevo proceso (proceso hijo)
child = subprocess.Popen(
    [sys.executable, "-c", "import time; time.sleep(1)"]
)


print("Child PID:", child.pid)

#esperamos a que el proceso hijo termine
child.wait()


print("Child return code:", child.returncode)