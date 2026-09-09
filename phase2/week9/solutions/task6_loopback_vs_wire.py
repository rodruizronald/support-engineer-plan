"""Task 6 — Loopback vs the wire, and a packet nobody catches (optional;
practices Q1, Q7, and Q9).

Goal: two parts.

  (a) Take psutil.net_io_counters(pernic=True) before and after fetching a
      URL, and print the per-interface deltas — the bytes show up on en0. Now
      do it again while sending a few kilobytes to Task 3's socket on
      127.0.0.1:8099 (start that script first): lo0 moves and en0 doesn't,
      which is loopback proving it never touches the hardware.

  (b) Open a SOCK_DGRAM socket with a 1-second timeout, connect() it to a port
      nothing is listening on, and send() a few bytes. The send SUCCEEDS —
      best-effort delivery hands out no receipts — and only the FOLLOWING
      recv() raises ConnectionRefusedError, because an ICMP port-unreachable
      came back after the fact. Compare that with TCP, which refuses at once.
"""

# TODO: implement this task.
print("Task 6 — not implemented yet. Watch the counters, then send a packet into the void!")
