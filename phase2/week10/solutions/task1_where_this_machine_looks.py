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
import sys
import socket
import dns.resolver
import dns.exception

hosts_path = "/etc/hosts"
if sys.platform == "win32":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

names = ["localhost", "example.com"]
print("Hosts file:", hosts_path)
with open(hosts_path) as hosts_file:
    for line in hosts_file:
        line = line.split("#", 1)[0].strip()
        if line:
            print(line)
            for name in line.split()[1:]:
                if name not in names:
                    names.append(name)

system = dns.resolver.Resolver()
print("\nSystem DNS servers:", system.nameservers)
print("Search domains:", [str(domain) for domain in system.search])

public = dns.resolver.Resolver(configure=False)
public.nameservers = ["8.8.8.8"]
public.lifetime = 3

for name in names:
    print("\nName:", name)
    try:
        addresses = set()
        for result in socket.getaddrinfo(name, 443):
            addresses.add(result[4][0])
        print("Application:", sorted(addresses))
    except socket.gaierror as error:
        print("Application error:", error)

    for record_type in ("A", "AAAA"):
        try:
            answer = public.resolve(name, record_type, search=False)
            print("8.8.8.8", record_type, [str(record) for record in answer])
        except dns.resolver.NXDOMAIN:
            print("8.8.8.8", record_type, "NXDOMAIN: name does not exist")
        except dns.resolver.NoAnswer:
            print("8.8.8.8", record_type, "NoAnswer: no records of this type")
        except dns.exception.DNSException as error:
            print("8.8.8.8", record_type, type(error).__name__, str(error))

# I learned that my computer and public DNS can give different answers for the same name.
