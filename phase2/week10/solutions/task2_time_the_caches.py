"""Task 2 — Time the cache hierarchy (practices Q2, Q4, and Q5).

Standard library only.

Goal: with time.perf_counter() around socket.getaddrinfo(), time five lookups
each of three names, and print every sample in milliseconds:

  (1) A name nobody has ever asked for, so every cache misses. A wildcard
      domain makes one for you:

          f"w10-{uuid.uuid4().hex[:8]}.127-0-0-1.sslip.io"

      resolves to 127.0.0.1 for any label you invent.

  (2) A popular name you haven't looked up in this session (pick a site you
      don't normally visit).

  (3) A random name that doesn't exist, e.g. f"{uuid.uuid4().hex[:8]}.python.org"
      — catch socket.gaierror and time the failure too.

On a real run: (1) cost ~300 ms the first time (full recursion) and ~1 ms
after (the OS cache). (2) cost ~35 ms the first time — one round trip to a
resolver that already had it — then ~1 ms. (3) failed slowly once and fast
after: the FAILURE was cached too. That's negative caching.

Set the three tiers next to Week 1's latency table. And notice that Python
itself caches nothing: even the ~1 ms hit is a request to another process
(mDNSResponder on macOS, the DNS Client service on Windows), which is why it
costs a millisecond and not a microsecond.

On Windows, run `ipconfig /displaydns` (or Get-DnsClientCache) right after,
and find your sslip.io name sitting in the OS cache with its TTL counting down.
"""

# TODO: implement this task.
import socket
import time
import uuid

names = [
    f"w10-{uuid.uuid4().hex[:8]}.127-0-0-1.sslip.io",
    "www.wikipedia.org",
    f"{uuid.uuid4().hex[:8]}.python.org",
]

for name in names:
    print("\nName:", name)
    for attempt in range(5):
        start = time.perf_counter()
        try:
            results = socket.getaddrinfo(name, 443)
            result = sorted({item[4][0] for item in results})
        except socket.gaierror as error:
            result = str(error)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"Lookup {attempt + 1}: {elapsed:.3f} ms", result)

"""
The new name took 518 ms at first, then about 0.3 ms.
Wikipedia took 56 ms at first, then less than 1 ms.
The missing name stayed around 50 ms.
Repeating successful lookups was faster because of caching.
Even 0.3 ms is about 3,000 times longer than the 100 ns RAM example from Week 1.
"""
