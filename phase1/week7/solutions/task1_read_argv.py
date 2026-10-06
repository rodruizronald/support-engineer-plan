"""Task 1 — See what the shell handed you (practices Q4 and Q6).

Goal: print len(sys.argv) and then each element of sys.argv on its own
numbered line. Now run it several ways and compare:

    python task1_read_argv.py a b c
    python task1_read_argv.py "two words"
    python task1_read_argv.py *.py

Watch the glob arrive as MANY arguments and the quoted string arrive as ONE —
proof that the shell rewrote your command line before Python ever saw it.
"""

import sys

print("Number of arguments:", len(sys.argv))

for index, argument in enumerate(sys.argv):
    print(index, argument)