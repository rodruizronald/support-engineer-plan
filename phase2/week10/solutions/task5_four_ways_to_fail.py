"""Task 5 — Make DNS fail four ways (practices Q5 and Q9).

Needs: pip install dnspython

Goal: with a dnspython resolver pointed at 8.8.8.8 and lifetime = 2, provoke
each failure shape and print the exception class name and how many
milliseconds it took to fail:

  NXDOMAIN   does-not-exist.python.org
  NODATA     github.com, type AAAA                    -> NoAnswer
  SERVFAIL   dnssec-failed.org (DNSSEC broken on
             purpose; a validating resolver refuses)  -> NoNameservers
  timeout    example.com, against a resolver at
             192.0.2.1 (documentation-only; nothing
             answers there)                           -> LifetimeTimeout

Then pass the first three names through socket.getaddrinfo() and print the
gaierror's errno and message. Notice how much the OS throws away: on macOS,
NXDOMAIN and NODATA both come back as the same errno 8.

dnssec-failed.org may SUCCEED through your system resolver. The ISP resolver
on the verifying machine doesn't check DNSSEC, so it handed back an address
that 8.8.8.8 and 1.1.1.1 both refused. Two resolvers, two verdicts, one name.

Two more things to notice:

  - The failures that come back in tens of milliseconds are ANSWERS. The
    timeout costs your full lifetime. Fast failure and slow failure point at
    different problems.

  - Bonus: try does-not-exist.example.com. You'd expect NXDOMAIN and get
    NoAnswer instead, because example.com is hosted on Cloudflare, which
    answers every nonexistent name with "exists, no records." Textbook
    categories meet real providers.
"""

# TODO: implement this task.
import socket
import time
import dns.resolver
import dns.exception

cases = [
    ("does-not-exist.python.org", "A", "8.8.8.8"),
    ("github.com", "AAAA", "8.8.8.8"),
    ("dnssec-failed.org", "A", "8.8.8.8"),
    ("example.com", "A", "192.0.2.1"),
    ("does-not-exist.example.com", "A", "8.8.8.8"),
]

for name, record_type, server in cases:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [server]
    resolver.lifetime = 2
    start = time.perf_counter()
    try:
        answer = resolver.resolve(name, record_type)
        result = [str(record) for record in answer]
    except dns.exception.DNSException as error:
        result = type(error).__name__ + ": " + str(error)
    elapsed = (time.perf_counter() - start) * 1000
    print(name, record_type, server, result, f"{elapsed:.2f} ms")

print("\nSystem resolver:")
for name in ("does-not-exist.python.org", "github.com", "dnssec-failed.org"):
    start = time.perf_counter()
    try:
        addresses = socket.getaddrinfo(name, 443)
        print(name, sorted({item[4][0] for item in addresses}))
    except socket.gaierror as error:
        print(name, "errno:", error.errno, "message:", error.strerror)
    print(f"Time: {(time.perf_counter() - start) * 1000:.2f} ms")

# I learned that a missing name is different from a DNS server that does not answer.
