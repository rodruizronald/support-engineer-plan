# Week 10 — Answers: DNS — Turning Names Into Addresses

Answer each question below in your own words. Don't copy-paste definitions; explain them as if to a friend.

## Part A — How a name becomes an address

### Q1. Why does DNS exist, and why is it a distributed hierarchy instead of one big file (`HOSTS.TXT`)? Read `www.github.com.` right to left and name the root, the TLD, and the domain. What is a zone, what does delegation mean, and what makes a server authoritative for a name?

_Your answer:_

### Q2. Walk the resolver chain: stub resolver → recursive resolver → root → TLD → authoritative. Who does the walking, what's the difference between a recursive and an iterative query, and at which steps can a cache answer instead? Why does almost no lookup ever reach a root server, and why does DNS normally travel over UDP (with TCP as a fallback)?

_Your answer:_

### Q3. Record types: A, AAAA, CNAME, MX, TXT, NS, SOA, PTR. What is each for, and what's one support ticket where each one is the answer? What does a CNAME chain do to debugging, why are CNAMEs so common in front of CDNs and SaaS products, and why can't one sit at a domain's apex? What does a PTR record prove, and what doesn't it?

_Your answer:_

### Q4. What is a TTL, who sets it, and which layers cache an answer for that long (all of them, between your Python process and the authoritative server)? Why is "DNS propagation" really TTL expiry, why does the TTL you see count down, how should a team plan a DNS change, and why might a long-running process never pick up a new address at all?

_Your answer:_

### Q5. Distinguish NXDOMAIN, NOERROR with no answer (NODATA), SERVFAIL, REFUSED, and no response at all (timeout), and say which component each implicates. What is negative caching, where does its duration come from (the SOA record), and why does a just-created name keep failing for a while? How do "the name is wrong" and "the resolver is unreachable" look different from Python, and in how long they take to fail?

_Your answer:_

## Part B — Where resolution is configured, and how it disagrees with itself

### Q6. Where does the hosts file live on macOS/Linux and on Windows, why is it consulted before DNS, and why is it both a favorite debugging trick and a classic cause of "works on my machine"? Is `localhost` a DNS name? Name one kind of software that edits your hosts file without asking.

_Your answer:_

### Q7. What do `nameserver`, `search`, `ndots`, and `timeout` do in `resolv.conf`? Use search domains to explain why `db` resolves on one machine and not another, and what `ndots:5` (Kubernetes' default) does to a lookup for `api.github.com`. Why is `/etc/resolv.conf` on macOS mostly a decoy, and where does Windows keep the same settings?

_Your answer:_

### Q8. Why does the same name resolve to a private address on the VPN and to a public address (or nothing) off it (split-horizon)? Where does a container's `/etc/resolv.conf` come from, what is Docker's embedded resolver at `127.0.0.11`, and why is "it works on my laptop but not in the container" so often a DNS story?

_Your answer:_

### Q9. Why can `dig` (or `nslookup`) and your application get different answers for the same name at the same moment? Contrast asking a DNS server directly with `getaddrinfo()`'s whole OS policy, then add the browser's own cache and DNS-over-HTTPS. When a customer says "DNS is fine, I checked," what exactly did they check?

_Your answer:_

### Q10. (Tie-back to Weeks 1, 5, 6, and 9.) Trace `socket.getaddrinfo("www.github.com", 443)` out and back: the config files the OS reads (Week 6), the process that actually does the lookup (Week 5), the UDP packet to port 53 and its ephemeral source port (Week 9), each cache that could answer instead, the CNAME, and the tuples that come back. Put a rough cost on each tier against Week 1's latency table, then name one realistic way each step fails.

_Your answer:_
