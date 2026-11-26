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
import random
import socket
import struct

for name in ("example.com", "does-not-exist.python.org"):
    query_id = random.randrange(65536)
    header = struct.pack("!HHHHHH", query_id, 0x0100, 1, 0, 0, 0)
    question = b""
    for label in name.split("."):
        encoded = label.encode("ascii")
        question += bytes([len(encoded)]) + encoded
    question += b"\x00" + struct.pack("!HH", 1, 1)
    query = header + question
    print("\nName:", name, "Query bytes:", len(query))

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
            connection.settimeout(2)
            connection.sendto(query, ("8.8.8.8", 53))
            reply, sender = connection.recvfrom(4096)
        if sender != ("8.8.8.8", 53) or len(reply) < 12:
            print("Unexpected reply")
            continue
        reply_id, flags, questions, answers, authority, additional = struct.unpack("!HHHHHH", reply[:12])
        if reply_id != query_id or not flags & 0x8000:
            print("Reply does not match the query")
            continue
        print("ID matches:", reply_id == query_id)
        print(f"Flags: {flags:04x}")
        print("Answers:", answers)
        print("RCODE:", flags & 0x000F)
        print("Hex:", reply.hex(" "))
    except OSError as error:
        print(type(error).__name__, str(error))

# I learned that a DNS lookup sends bytes, and the reply contains answers or an error code.
