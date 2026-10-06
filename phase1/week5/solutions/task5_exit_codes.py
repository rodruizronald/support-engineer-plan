"""Task 5 — Exit codes (practices Q9).

Goal: write a script that exits with a code you choose via sys.exit(3). Run
it, then in the shell run `echo $?` to see the OS report that code. Then,
from Python, launch a child with subprocess.run([...]) and read its
.returncode. See how a program tells whoever launched it whether it worked.
"""


import subprocess
import sys 

result = subprocess.run(
    [sys.executable, "-c", "import sys; sys.exit(3)"]
)

print (f"Child process exit code:", result.returncode)

sys.exit(3) 
