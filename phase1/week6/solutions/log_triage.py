"""Mini-project — log-triage.

A small CLI tool that does what a support engineer does in the first minute
with a log file: figure out what the file is, find out what's in it without
loading it into RAM, and read the end of it. Given a path to a log file, it
reports three things. Tasks 1, 2, 3, 4, and 5 give you the building blocks —
text vs bytes, pathlib, streaming reads, metadata, and I/O errors — and this
project joins them into one triage tool.

  Section 1 — What this file is: the resolved absolute path, the size in both
  MB and MiB, the last modification time plus how long ago that was, and the
  permission bits.

  Section 2 — What's inside (streamed): total line count, a count per log
  level (ERROR / WARN / INFO / DEBUG), the first and last timestamp seen, and
  the peak memory used while scanning — proving you can scan a file far
  bigger than the RAM you spent on it.

  Section 3 — The last N lines: a tail (default 10) kept in a fixed-size
  collections.deque(maxlen=N), so memory stays flat no matter how big the
  file is.

This is the sixth artifact in your GitHub portfolio. See the Phase 1 README
(Graduation Projects) for the expected output format.
"""

# TODO: implement the mini-project.
print("log-triage — not implemented yet. Build your log file triage tool here!")
