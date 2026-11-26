"""Task 4 — Three resolvers, three clocks (practices Q4 and Q9).

Needs: pip install dnspython

Goal: build three dnspython resolvers — the system one (Resolver()),
8.8.8.8, and 1.1.1.1 (Resolver(configure=False) with nameservers set). For
github.com and www.microsoft.com, resolve A from each and print the sorted
addresses, answer.rrset.ttl, answer.canonical_name, and the milliseconds it
took. time.sleep(5), then do it all again.

Things to look for, all seen on a real run:

  - The TTL from one resolver drops by about 5 between rounds. It's the time
    REMAINING in that cache, not the record's setting.

  - 8.8.8.8 may not count down cleanly, because it isn't one cache. It's a
    fleet of caches behind one anycast address.

  - The resolvers give DIFFERENT addresses for www.microsoft.com, because a
    CDN answers based on where the resolver is. Disagreement is not
    automatically a fault.

  - canonical_name shows the end of the CNAME chain without you following it.

  - One sample may take ~2 seconds. That's a UDP packet that got lost and
    dnspython's retry — Week 9's best-effort delivery, showing up in your own
    timings.
"""

# TODO: implement this task.
import time
import dns.resolver
import dns.exception

resolvers = {"System": dns.resolver.Resolver()}
for address in ("8.8.8.8", "1.1.1.1"):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [address]
    resolvers[address] = resolver

for round_number in range(2):
    print("\nRound:", round_number + 1)
    for name in ("github.com", "www.microsoft.com"):
        for label, resolver in resolvers.items():
            start = time.perf_counter()
            try:
                answer = resolver.resolve(name, "A", lifetime=3)
                elapsed = (time.perf_counter() - start) * 1000
                print(name, label)
                print("Addresses:", sorted(str(record) for record in answer))
                print("TTL:", answer.rrset.ttl)
                print("Canonical name:", answer.canonical_name)
                print(f"Time: {elapsed:.2f} ms")
            except dns.exception.DNSException as error:
                elapsed = (time.perf_counter() - start) * 1000
                print(name, label, type(error).__name__, f"{elapsed:.2f} ms")
    if round_number == 0:
        time.sleep(5)

# I learned that DNS servers can return different addresses and different remaining cache times.
