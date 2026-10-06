"""Task 1 — Every address this machine has (practices Q2, Q4, and Q7).

Goal: using psutil.net_if_addrs() and psutil.net_if_stats(), print one block
per interface: the MAC (family psutil.AF_LINK), the IPv4 address with its
netmask, any IPv6 addresses, and whether the interface is up plus its MTU.
Find lo0 and en0 in the output.

Two details are worth a sentence each in your notes, because both are lessons
rather than quirks:

  - Loopback's MTU is enormous (~16384) next to en0's 1500. There is no wire
    and therefore no frame size to respect.

  - stats.speed reads 0 on macOS. The OS simply won't tell you — noticing
    which facts you can and can't get is part of the job.
"""

# TODO: implement this task.
import socket
import psutil

addresses = psutil.net_if_addrs()
stats = psutil.net_if_stats()

for name, items in addresses.items():
    print("\nInterface:", name)
    for address in items:
        if address.family == psutil.AF_LINK:
            print("MAC:", address.address)
        elif address.family == socket.AF_INET:
            print("IPv4:", address.address, "Netmask:", address.netmask)
        elif address.family == socket.AF_INET6:
            print("IPv6:", address.address)
    if name in stats:
        print("Up:", stats[name].isup)
        print("MTU:", stats[name].mtu)
        print("Speed:", stats[name].speed, "Mbps")
