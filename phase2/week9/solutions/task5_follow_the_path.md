# Task 5 — Follow the path out of your house

*(Practices Q3 and Q5. This is a shell task: run each command, paste its real
output, and write a couple of sentences on what it proved.)*

## 1. The routing table — where does everything go?

```
$ netstat -rn -f inet | head
```

_Paste output here._

**What it showed me:** _which row is the `default` route, what my gateway
address is, and which interface packets leave by._

## 2. The default route in detail

```
$ route -n get default
```

_Paste output here._

**What it showed me:** _the same gateway, plus the interface and the MTU._

## 3. Can I reach my own router?

```
$ ping -c 3 <your-gateway>
```

_Paste output here._

**What it showed me:** _the round trip to the first hop — the floor under
every other measurement. If it times out, see the note below._

## 4. The whole path to a distant host

```
$ traceroute -n -q 1 -w 1 example.com
```

_Paste output here._

**What it showed me:** _which hop is my own router, where the latency jumps
(that's usually the leap out of my ISP), and where stars appear._

## Two surprises to account for

1. **A gateway that ignores `ping` but answers traceroute's hop 1.** Filtered
   ICMP is not a down host — and mistaking one for the other is a classic
   false alarm. Note whether this happened to you and how you know the
   gateway is fine anyway.
2. **Hops with `10.x` addresses.** Q4's private ranges are in use inside your
   ISP's own network too, so a private address in the middle of a traceroute
   is normal, not a misconfiguration.
