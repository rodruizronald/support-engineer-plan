# Week 9 — Answers: The Network as Hardware — Packets, Addresses, and Ports

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The wire, the addresses, and the route

### Q1. What is a packet, and what's the difference between its header and its payload? What is an interface's MTU (~1500 bytes), and what does that imply about transferring a 1 GB file? The network is best-effort: what is it allowed to do to your packet, and why was designing it that way — instead of guaranteeing delivery — the right call?

_Answer: _A packet is a small unit of data that travels through a network. The header contains information like the source and destination addresses, while the payload contains the actual data. The MTU is the maximum packet size an interface can carry, usually around 1500 bytes. Because of this, a 1 GB file must be divided into many packets. The network is “best-effort,” so packets can be lost, delayed, duplicated, or arrive out of order. This keeps the network simple and efficient, while protocols like TCP can handle reliable delivery.__

### Q2. What does a MAC address identify, and what does an IP address identify? Which one is rewritten at every hop and which survives the whole trip, what is ARP for, and why does a machine need both?

_Answer: A MAC address identifies a network interface on the local network, while an IP address identifies where a device is on a network. The MAC addresses change at each hop, but the source and destination IP addresses normally stay the same. ARP finds the MAC address associated with an IP address on the local network. We need both because IP helps reach the correct network, while MAC helps deliver data on the local network._

### Q3. What does a router actually do with a packet that arrives? What's in your machine's routing table, what is the default gateway, and what is the one decision the table exists to make? What is a hop, how does `traceroute` abuse TTL to reveal the path, and why can the return path differ from the outbound one?

_Answer: When a router receives a packet, it checks the destination IP and decides where to send it next. The routing table contains information about known networks and how to reach them. The default gateway is used when there is no more specific route. A hop is each router a packet passes through. `traceroute` uses TTL to make routers respond one by one and reveal the path. The return path can be different because routers make their own routing decisions._

### Q4. IPv4 vs IPv6, and what does a subnet mask / CIDR suffix (`/24`) tell your machine? What are the private address ranges, and what does NAT do to a packet on its way out and its way back? Why does a web server log an address that appears nowhere on your laptop, and what did NAT make hard?

_Answer: IPv4 uses 32-bit addresses and IPv6 uses 128-bit addresses, so IPv6 provides many more addresses. A subnet mask or `/24` tells the machine which part of an IP address represents the network. The main private IPv4 ranges are `10.x.x.x`, `172.16.x.x–172.31.x.x`, and `192.168.x.x`. NAT changes a private address to a public address when traffic goes to the Internet and reverses the process for the reply. This is why a web server usually sees your router's public IP instead of your computer's private IP. NAT also makes direct incoming connections to devices inside a private network harder._

### Q5. "The network is slow" is three separate claims. Define latency, bandwidth, and loss (plus jitter) with a physical cause for each. Using Week 1's latency hierarchy, explain why 20 sequential requests at 50 ms per round trip take a full second regardless of link speed — and why a host that doesn't answer `ping` is not necessarily down.

_Answer: Latency is the time data takes to travel, and distance or routers can increase it. Bandwidth is how much data can be transferred in a certain time and depends on the connection capacity. Loss happens when some packets do not arrive, for example because of congestion. Jitter is variation in latency. If we make 20 requests one after another and each takes 50 ms, they take about one second even with high bandwidth. Also, a host that does not answer `ping` is not necessarily down because a firewall may block ICMP._

## Part B — How your machine and your Python show you this

### Q6. What problem do ports solve that IP addresses don't? Explain the well-known and ephemeral ranges, and the four-tuple that identifies one connection. Why can't two programs listen on the same port while one server holds thousands of connections on a single port — and why does your outbound request also consume a port?

_Answer: An IP address identifies a machine, but ports identify which program or service should receive the data. Well-known ports are `0–1023` and are normally used for common services. Ephemeral ports are temporary ports normally used for outgoing connections. A connection is identified by four values: source IP, source port, destination IP, and destination port. Two programs normally cannot listen on the same address and port at the same time, but a server can have thousands of connections on one port because every connection has a different four-tuple. An outgoing connection also needs a temporary source port._

### Q7. What's the difference between listening on `127.0.0.1`, on `0.0.0.0`, and on one specific interface address? What is loopback, and does traffic to it reach the NIC at all? Explain "it works on my machine but nothing else can reach it" in these terms — and why your machine's hostname is not an address.

_Answer: `127.0.0.1` allows connections only from the same computer. `0.0.0.0` makes the program listen on all available interfaces, while a specific IP makes it listen only on that interface. Loopback is communication from the computer to itself, and that traffic does not physically reach the network card. This is why something can work on my computer but not be reachable from another computer if it only listens on `127.0.0.1`. A hostname is a name that can resolve to an address, but it is not the address itself._

### Q8. A socket is a file descriptor (Week 5). What does that buy you in practice, which OS calls therefore treat it like a file, and what does that have to do with `lsof`? What is the OS doing while your program sits blocked in `recv()`, and what exactly is a timeout protecting you from?

_Answer: A socket has a file descriptor, so the operating system can manage it like other open resources using operations such as `read`, `write`, and `close`. This is why tools like `lsof` can show open sockets. When a program is blocked in `recv()`, the operating system waits for data, so the program does not need to keep using the CPU. A timeout prevents the program from waiting forever if the data never arrives._

### Q9. What does TCP add on top of best-effort delivery, and what does UDP deliberately refuse to add? Name one thing each is the right choice for. (Weeks 11–12 go deep — here, just the contract.)

_Answer: TCP adds reliable and ordered delivery on top of a network that does not guarantee delivery. If data is lost, TCP can retransmit it. It is a good choice for web pages or file transfers. UDP does not guarantee delivery, order, or retransmissions, but it has less overhead and can be faster. It is useful for real-time applications like voice calls or some games._

### Q10. (Tie-back to Weeks 1, 3, 5, and 6.) Trace `urllib.request.urlopen("http://example.com")` all the way out and back: the name turned into an address, the socket and the file descriptor the OS returns (Week 5), the source and destination address and port, the packets leaving the NIC, the hops, the reply packets, the bytes copied into your process (Week 2), and the object in RAM with a name bound to it (Week 3). Then name one realistic way each step fails.

_Answer: When I run `urllib.request.urlopen("http://example.com")`, DNS first turns `example.com` into an IP address. Then the operating system creates a socket and gives the program a file descriptor. The connection has a source IP and port and a destination IP and port. The data is divided into packets that leave through the network interface and pass through routers until they reach the server. The server replies and the packets come back. The operating system receives the data and copies it into the process memory, where Python creates objects in RAM and binds names to them. DNS can fail, the socket or connection can fail, the network or a router can have problems, the server may not respond, a timeout can happen, or the program can fail while processing the response._
