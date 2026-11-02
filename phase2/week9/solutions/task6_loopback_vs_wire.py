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
import socket
import urllib.request
import psutil

for target in ("Internet", "Loopback"):
    before = psutil.net_io_counters(pernic=True)
    try:
        if target == "Internet":
            with urllib.request.urlopen("https://example.com", timeout=5) as response:
                response.read()
        else:
            with socket.create_connection(("127.0.0.1", 8099), timeout=2) as connection:
                connection.sendall(b"hello" * 1000)
    except OSError as error:
        print(target, "error:", error)
    after = psutil.net_io_counters(pernic=True)
    print("\n", target)
    for name in before:
        if name in after:
            sent = after[name].bytes_sent - before[name].bytes_sent
            received = after[name].bytes_recv - before[name].bytes_recv
            print(name, "Sent:", sent, "Received:", received)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
    connection.bind(("127.0.0.1", 0))
    unused_port = connection.getsockname()[1]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
    connection.settimeout(1)
    connection.connect(("127.0.0.1", unused_port))
    print("\nUDP sent:", connection.send(b"hello"))
    try:
        print("UDP reply:", connection.recv(1024))
    except OSError as error:
        print("UDP receive:", error)

try:
    with socket.create_connection(("127.0.0.1", unused_port), timeout=1):
        print("TCP connected")
except OSError as error:
    print("TCP connection:", error)
