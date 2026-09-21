"""Task 4 — Time a round trip honestly (practices Q5).

Goal: resolve one host to an IP once with socket.getaddrinfo(), then time five
socket.create_connection() calls to that IP (timeout=2) with
time.perf_counter(), printing min/avg/max in milliseconds. Do it for a nearby
host and a distant one, then print how long 20 sequential round trips would
cost at your measured average.

Two things to look for:

  - If you connect by NAME instead of by IP, your first sample is badly
    inflated because it includes the name lookup (~190 ms vs ~65 ms after, on
    a real run). That is exactly why you resolve first — and a preview of
    Week 10.

  - Set your result next to Week 1's numbers. One round trip buys you roughly
    a million RAM accesses, which is why 20 requests in a row cost a second no
    matter how fast the link is.
"""

# TODO: implement this task.
print("Task 4 — not implemented yet. Measure a real round trip here!")
