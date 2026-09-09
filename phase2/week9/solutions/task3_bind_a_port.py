"""Task 3 — Bind a port, then find it in the OS's tables (practices Q6, Q7, Q8).

Goal: bind a TCP socket to 127.0.0.1:8099, call listen(), print getsockname()
and fileno(), then park the script on input("press enter to release the
port... ").

While it waits, in a second terminal run:

    lsof -nP -iTCP:8099
    netstat -an -p tcp | grep 8099

Look at lsof's FD column: it's the same small integer your script printed —
Week 5's file descriptor, now with an address attached. (macOS writes the
address as 127.0.0.1.8099, with a dot before the port, so grep for the number
rather than for a colon.)

Then, while the first copy is still holding the port, run a second copy of
this script and read the error you get.
"""

# TODO: implement this task.
print("Task 3 — not implemented yet. Bind a port and go find it in the OS's tables!")
