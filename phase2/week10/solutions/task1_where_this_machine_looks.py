r"""Task 1 — Where this machine looks, and what your program actually gets
(practices Q6, Q7, and Q9).

Needs: pip install dnspython

Goal: two parts.

  (a) Print the active (non-comment) lines of your hosts file — /etc/hosts,
      or C:\Windows\System32\drivers\etc\hosts on Windows (choose with
      sys.platform). Then print the system's resolver list and search domains
      via dns.resolver.Resolver().nameservers and .search — dnspython reads
      the right place on each OS, so you don't have to.

  (b) For localhost, example.com, and any extra name your hosts file lists,
      print the unique addresses socket.getaddrinfo(name, 443) returns (what
      your APPLICATION gets) next to what 8.8.8.8 says for A and AAAA (a
      Resolver(configure=False) with nameservers = ["8.8.8.8"]; catch
      dns.resolver.NXDOMAIN and dns.resolver.NoAnswer).

Three disagreements to look for, each one a lesson:

  - localhost: your program gets 127.0.0.1 and ::1; public DNS says NXDOMAIN.
    The answer never left your machine.

  - A hosts-file line some other tool added (Docker Desktop adds
    kubernetes.docker.internal): it resolves for you, and for nobody else.

  - example.com: public DNS has AAAA records, but if this machine has no
    global IPv6 address, getaddrinfo() may hand back IPv4 only. The OS doesn't
    ask for what it can't use (on macOS, `scutil --dns` says "Request A
    records").

On Windows the hosts file is usually all comments, because Windows answers
localhost internally — same answer, different mechanism.
"""

# TODO: implement this task.
print("Task 1 — not implemented yet. Compare what your program gets with what DNS says!")
