"""Task 6 — Watch buffering swallow your logs (optional — practices Q9).

Goal: print five lines in a loop with a time.sleep(1) between them.

Run it straight in the terminal: the lines appear one per second. Now pipe it:

    python task6_buffering.py | cat

and watch them sit invisible, then arrive ALL AT ONCE at the end — because
stdout switched from line-buffered to block-buffered the moment it stopped
being a terminal. (Printing sys.stdout.isatty() shows you which mode you're
in.) Then fix it three ways and confirm each one works:

    print(..., flush=True)
    python -u task6_buffering.py | cat
    PYTHONUNBUFFERED=1 python task6_buffering.py | cat

This is exactly why a container's logs look empty right up until it dies.

This task is optional — a stretch for when you want to go further.
"""

# TODO: implement this task (optional).
print("Task 6 — not implemented yet. Make buffering visible, then defeat it!")
