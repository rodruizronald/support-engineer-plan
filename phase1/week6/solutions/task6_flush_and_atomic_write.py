"""Task 6 — Buffering, flushing, and an atomic write (optional — practices
Q4 and Q9).

Goal: two parts.

  (a) Open a file for writing, write a line without closing it, and
  immediately try to read the file from a second handle — see nothing there
  yet; then call .flush() and read again to watch it appear.

  (b) Do a safe write: write the new contents to config.tmp, then
  os.replace("config.tmp", "config.json") to swap it into place in one atomic
  step, so a reader can never catch a half-written file.

This task is optional — a stretch for when you want to go further.
"""

# TODO: implement this task (optional).
print("Task 6 — not implemented yet. Watch a buffer flush, then write atomically here!")
