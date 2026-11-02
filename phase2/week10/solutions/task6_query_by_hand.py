r"""Task 6 — A DNS query by hand (optional; practices Q2 and Q5, plus Weeks 2
and 9).

Standard library only — no DNS library allowed.

Goal: build the query bytes yourself.

  - A 12-byte header:
        struct.pack("!HHHHHH", query_id, 0x0100, 1, 0, 0, 0)
    a random ID, the "recursion desired" flag, and one question.
  - The name as length-prefixed labels: b"\x07example\x03com\x00"
  - Type A, class IN: struct.pack("!HH", 1, 1)

That's 29 bytes for example.com. Send it with a SOCK_DGRAM socket to
("8.8.8.8", 53) with a 2-second timeout, recvfrom() the reply, and unpack its
first 12 bytes the same way: check the ID matches, read the answer count,
and read the RCODE from the low 4 bits of the flags.

Print the reply as a hex dump (Week 2's habit) and find, by eye:

  - your name echoed back:  07 65 78 61 6d 70 6c 65 03 63 6f 6d 00
  - c0 0c — a pointer back to byte 12, so the name isn't repeated
  - the 4-byte TTL
  - the 4 bytes of each address

Then ask for does-not-exist.python.org: the flags change from 81 80 to
81 83. NXDOMAIN is one nibble, 3. Every "DNS error" you will ever see in a
ticket started as that nibble.
"""

# TODO: implement this task.
print("Task 6 — not implemented yet. Hand-build a DNS query and read the reply!")
