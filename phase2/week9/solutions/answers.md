# Week 9 — Answers: The Network as Hardware — Packets, Addresses, and Ports

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The wire, the addresses, and the route

### Q1. What is a packet, and what's the difference between its header and its payload? What is an interface's MTU (~1500 bytes), and what does that imply about transferring a 1 GB file? The network is best-effort: what is it allowed to do to your packet, and why was designing it that way — instead of guaranteeing delivery — the right call?

_Your answer:_

### Q2. What does a MAC address identify, and what does an IP address identify? Which one is rewritten at every hop and which survives the whole trip, what is ARP for, and why does a machine need both?

_Your answer:_

### Q3. What does a router actually do with a packet that arrives? What's in your machine's routing table, what is the default gateway, and what is the one decision the table exists to make? What is a hop, how does `traceroute` abuse TTL to reveal the path, and why can the return path differ from the outbound one?

_Your answer:_

### Q4. IPv4 vs IPv6, and what does a subnet mask / CIDR suffix (`/24`) tell your machine? What are the private address ranges, and what does NAT do to a packet on its way out and its way back? Why does a web server log an address that appears nowhere on your laptop, and what did NAT make hard?

_Your answer:_

### Q5. "The network is slow" is three separate claims. Define latency, bandwidth, and loss (plus jitter) with a physical cause for each. Using Week 1's latency hierarchy, explain why 20 sequential requests at 50 ms per round trip take a full second regardless of link speed — and why a host that doesn't answer `ping` is not necessarily down.

_Your answer:_

## Part B — How your machine and your Python show you this

### Q6. What problem do ports solve that IP addresses don't? Explain the well-known and ephemeral ranges, and the four-tuple that identifies one connection. Why can't two programs listen on the same port while one server holds thousands of connections on a single port — and why does your outbound request also consume a port?

_Your answer:_

### Q7. What's the difference between listening on `127.0.0.1`, on `0.0.0.0`, and on one specific interface address? What is loopback, and does traffic to it reach the NIC at all? Explain "it works on my machine but nothing else can reach it" in these terms — and why your machine's hostname is not an address.

_Your answer:_

### Q8. A socket is a file descriptor (Week 5). What does that buy you in practice, which OS calls therefore treat it like a file, and what does that have to do with `lsof`? What is the OS doing while your program sits blocked in `recv()`, and what exactly is a timeout protecting you from?

_Your answer:_

### Q9. What does TCP add on top of best-effort delivery, and what does UDP deliberately refuse to add? Name one thing each is the right choice for. (Weeks 11–12 go deep — here, just the contract.)

_Your answer:_

### Q10. (Tie-back to Weeks 1, 3, 5, and 6.) Trace `urllib.request.urlopen("http://example.com")` all the way out and back: the name turned into an address, the socket and the file descriptor the OS returns (Week 5), the source and destination address and port, the packets leaving the NIC, the hops, the reply packets, the bytes copied into your process (Week 2), and the object in RAM with a name bound to it (Week 3). Then name one realistic way each step fails.

_Your answer:_
