"""Mini-project — encoding-doctor.

A small CLI tool that does what a support engineer does when a file shows up
full of garbled characters: look at the bytes and figure out how to read
them. Given a string (or a small file), it reports three things:

  Section 1 — What is this data: number of characters vs number of bytes
  (UTF-8), whether every character is plain ASCII, and any non-ASCII
  characters flagged with their Unicode code point.

  Section 2 — Hex view: a hexdump-style view of the first N bytes (offset,
  hex bytes, and an ASCII gutter), like the left columns of xxd.

  Section 3 — Encoding sanity check: try decoding the bytes as ASCII,
  latin-1, and UTF-8, and report which succeed and which raise — so you can
  see why the same bytes look fine in one tool and garbled in another.

This is the second artifact in your GitHub portfolio. See the Phase 1 README
(Graduation Projects) for the expected output format.
"""

# TODO: implement the mini-project.
print("encoding-doctor — not implemented yet. Build your byte/encoding inspector here!")
