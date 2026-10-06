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
import socket
import urllib.request

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as connection:
    connection.connect(("8.8.8.8", 80))
    print("Local IP and port:", connection.getsockname())

try:
    with urllib.request.urlopen("https://api.ipify.org", timeout=5) as response:
        print("Public IP:", response.read().decode())
except OSError as error:
    print("Public IP error:", error)

try:
    print("Hostname IP:", socket.gethostbyname(socket.gethostname()))
except socket.gaierror as error:
    print("Hostname error:", error)
