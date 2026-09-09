"""Mini-project — net-snapshot.

A small CLI tool that answers the first three questions a support engineer
asks about a machine's place on the network: what are its addresses, who is
listening on it, and how far away is everything else. Tasks 1, 2, 3, and 4
give you the building blocks — interfaces and MTUs, the private-vs-public
address gap, bound ports and file descriptors, and honest round-trip timing —
and this project joins them into one tool.

  Section 1 — This machine on the network: hostname, then one line per active
  interface with its IPv4/netmask, MAC, and MTU; the default gateway; the
  source address the OS would use to reach the internet; and the public
  address the internet actually sees (the NAT line).

  Section 2 — Who's listening here: every listening TCP port, with the address
  it is bound to, and a flag saying whether that binding is local-only
  (127.0.0.1) or reachable from the network (0.0.0.0). This is the "why can't
  anything connect to it" section.

  Section 3 — Where the time goes: TCP round trips to loopback, the gateway,
  a nearby host, and a distant one, as min/avg/max, with a slowdown column
  against Week 1's memory figure and the cost of 20 sequential round trips.

This is the first artifact of Phase 2 in your GitHub portfolio, and the direct
ancestor of the request-doctor you build in Week 20. See the Phase 2 README
(Graduation Projects) for the expected output format.
"""

# TODO: implement the mini-project.
print("net-snapshot — not implemented yet. Build your network snapshot tool here!")
