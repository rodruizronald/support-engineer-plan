"""Task 2 — Which address does the world see? (practices Q4 and Q7).

Goal: three short parts.

  (a) Ask the OS which source address it would use to reach the internet:
      open a SOCK_DGRAM socket, connect(("8.8.8.8", 80)) — a UDP connect()
      sends no packets at all, it just makes the OS consult the routing
      table — and print getsockname(). Note the high ephemeral port it also
      picked.

  (b) Fetch https://api.ipify.org and print the address the server saw.
      Compare the two: your private address, its public one. That gap is NAT.

  (c) Try the textbook idiom socket.gethostbyname(socket.gethostname()) and
      watch it raise gaierror on macOS, because your .local hostname isn't in
      DNS. Your hostname is not an address.
"""

# TODO: implement this task.
print("Task 2 — not implemented yet. Compare your private address with your public one here!")
