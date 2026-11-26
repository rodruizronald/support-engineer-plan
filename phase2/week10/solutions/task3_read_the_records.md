# Task 3 — Read the records, then walk the tree yourself

*(Practices Q1, Q2, and Q3. This is a shell task: run each command, paste its
real output, and write a couple of sentences on what it proved.)*

> **On Windows** there's no `dig`. Use `Resolve-DnsName` for 1–3 (`-Type MX`,
> `-Type NS`, `-Type SOA`; `Resolve-DnsName www.microsoft.com` shows the
> chain; `Resolve-DnsName 8.8.8.8` does the PTR), and do section 4 by hand:
> it's the same walk `+trace` automates. Paste whichever commands you
> actually ran.

## 1. The everyday records

```
$ dig +noall +answer github.com A github.com AAAA github.com MX github.com NS github.com SOA
```

```powershell
Resolve-DnsName github.com -Type A
```

```text
Name                                           Type   TTL   Section    IPAddress
.....                                           ....   ...   .......    .........
github.com                                     A      57    Answer     140.82.113.4
```

```powershell
Resolve-DnsName github.com -Type AAAA
```

```text
Name                        Type TTL   Section    PrimaryServer               NameAdministrator           SerialNumber
....                        .... ...   .......    .............               .................           ............
github.com                  SOA  3583  Authority  dns1.p08.nsone.net          hostmaster.nsone.net        1656468023
```

```powershell
Resolve-DnsName github.com -Type MX
```

```text
Name                                     Type   TTL   Section    NameExchange                              Preference
....                                     ....   ...   .......    ............                              ..........
github.com                               MX     300   Answer     github-com.mail.protection.outlook.com    0
```

```powershell
Resolve-DnsName github.com -Type NS
```

```text
Name                           Type   TTL   Section    NameHost
....                           ....   ...   .......    ........
github.com                     NS     3131  Answer     dns1.p08.nsone.net
github.com                     NS     3131  Answer     dns2.p08.nsone.net
github.com                     NS     3131  Answer     dns3.p08.nsone.net
github.com                     NS     3131  Answer     dns4.p08.nsone.net
github.com                     NS     3131  Answer     ns-1283.awsdns-32.org
github.com                     NS     3131  Answer     ns-1707.awsdns-21.co.uk
github.com                     NS     3131  Answer     ns-421.awsdns-52.com
github.com                     NS     3131  Answer     ns-520.awsdns-01.net
```

```powershell
Resolve-DnsName github.com -Type SOA
```

```text
Name                        Type TTL   Section    PrimaryServer               NameAdministrator           SerialNumber
....                        .... ...   .......    .............               .................           ............
github.com                  SOA  900   Answer     ns-1707.awsdns-21.co.uk     awsdns-hostmaster.amazon.co 1
                                                                              m
```

_Answer: I received A, MX, NS, and SOA records. The AAAA query returned SOA information but no IPv6 address. The MX points to Microsoft Outlook, and the NS names show NS1 and AWS DNS servers._

**What it showed me:** _which record types came back and which didn't (look
for the AAAA line), who handles this company's email, and how many different
DNS providers serve the zone._

## 2. A CNAME chain

```
$ dig +noall +answer www.microsoft.com
```

```powershell
Resolve-DnsName www.microsoft.com
```

```text
Name                           Type   TTL   Section    NameHost
....                           ....   ...   .......    ........
www.microsoft.com              CNAME  891   Answer     www.microsoft.com-c-3.edgekey.net
www.microsoft.com-c-3.edgekey. CNAME  891   Answer     e13678.dscb.akamaiedge.net
net

Name       : e13678.dscb.akamaiedge.net
QueryType  : AAAA
TTL        : 11
Section    : Answer
IP6Address : 2600:1403:d400:e92::356e


Name       : e13678.dscb.akamaiedge.net
QueryType  : AAAA
TTL        : 11
Section    : Answer
IP6Address : 2600:1403:d400:e9b::356e


Name       : e13678.dscb.akamaiedge.net
QueryType  : AAAA
TTL        : 11
Section    : Answer
IP6Address : 2600:1403:d400:e98::356e


Name       : e13678.dscb.akamaiedge.net
QueryType  : A
TTL        : 10
Section    : Answer
IP4Address : 23.56.178.80
```

_Answer: Two CNAMEs led to an Akamai name. The aliases had a TTL of 891 seconds, while the final addresses had only 10 or 11 seconds left._

**What it showed me:** _how many aliases sit between the name I asked for and
an address, whose name the address finally belongs to, and what happens to
the TTL at each hop._

## 3. Reverse DNS

```
$ dig +short -x 8.8.8.8
```

```powershell
Resolve-DnsName 8.8.8.8
```

```text
Name                           Type   TTL   Section    NameHost
....                           ....   ...   .......    ........
8.8.8.8.in-addr.arpa           PTR    83003 Answer     dns.google
```

_Answer: 8.8.8.8 returned dns.google. This is its configured reverse name, not proof that a connection is safe._

**What it showed me:** _what name this address maps back to, and what that
does (and doesn't) prove about who I'm talking to._

## 4. The whole walk, from the root

```
$ dig +trace +nodnssec @1.1.1.1 example.com
```

_On Windows, the same walk by hand:_

```
> Resolve-DnsName example.com -Server a.root-servers.net -NoRecursion
> Resolve-DnsName example.com -Server <one of the com servers it named> -NoRecursion
> Resolve-DnsName example.com -Server <one of example.com's own servers> -NoRecursion
```

```powershell
Resolve-DnsName example.com -Type A -Server a.root-servers.net -NoRecursion
```

```text
Name                           Type   TTL   Section    NameHost
....                           ....   ...   .......    ........
com                            NS     17280 Authority  l.gtld-servers.net
                                      0
com                            NS     17280 Authority  j.gtld-servers.net
                                      0
com                            NS     17280 Authority  h.gtld-servers.net
                                      0
com                            NS     17280 Authority  d.gtld-servers.net
                                      0
com                            NS     17280 Authority  b.gtld-servers.net
                                      0
com                            NS     17280 Authority  f.gtld-servers.net
                                      0
com                            NS     17280 Authority  k.gtld-servers.net
                                      0
com                            NS     17280 Authority  m.gtld-servers.net
                                      0
com                            NS     17280 Authority  i.gtld-servers.net
                                      0
com                            NS     17280 Authority  g.gtld-servers.net
                                      0
com                            NS     17280 Authority  a.gtld-servers.net
                                      0
com                            NS     17280 Authority  c.gtld-servers.net
                                      0
com                            NS     17280 Authority  e.gtld-servers.net
                                      0

Name       : l.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.41.162.30


Name       : l.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:500:d937::30


Name       : j.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.48.79.30


Name       : j.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:502:7094::30


Name       : h.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.54.112.30


Name       : h.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:502:8cc::30


Name       : d.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.31.80.30


Name       : d.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:500:856e::30


Name       : b.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.33.14.30


Name       : b.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:503:231d::2:30


Name       : f.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.35.51.30


Name       : f.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:503:d414::30


Name       : k.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.52.178.30


Name       : k.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:503:d2d::30


Name       : m.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.55.83.30


Name       : m.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:501:b1f9::30


Name       : i.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.43.172.30


Name       : i.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:503:39c1::30


Name       : g.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.42.93.30


Name       : g.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:503:eea3::30


Name       : a.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.5.6.30


Name       : a.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:503:a83e::2:30


Name       : c.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.26.92.30


Name       : c.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:503:83eb::30


Name       : e.gtld-servers.net
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 192.12.94.30


Name       : e.gtld-servers.net
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2001:502:1ca1::30
```

```powershell
Resolve-DnsName example.com -Type A -Server 192.41.162.30 -NoRecursion -DnsOnly
```

```text
Resolve-DnsName:
Line |
   4 |  $records = Resolve-DnsName example.com -Type A -Server 192.41.162.30  …
     |             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     | example.com : Error de servidor DNS.
```

```powershell
Resolve-DnsName example.com -Type A -Server 192.5.6.30 -NoRecursion -TcpOnly -DnsOnly
```

```text
Name                           Type   TTL   Section    NameHost
....                           ....   ...   .......    ........
example.com                    NS     17280 Authority  hera.ns.cloudflare.com
                                      0
example.com                    NS     17280 Authority  elliott.ns.cloudflare.com
                                      0

Name       : hera.ns.cloudflare.com
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 108.162.192.162


Name       : hera.ns.cloudflare.com
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 172.64.32.162


Name       : hera.ns.cloudflare.com
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 173.245.58.162


Name       : hera.ns.cloudflare.com
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2606:4700:50::adf5:3aa2


Name       : hera.ns.cloudflare.com
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2803:f800:50::6ca2:c0a2


Name       : hera.ns.cloudflare.com
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2a06:98c1:50::ac40:20a2


Name       : elliott.ns.cloudflare.com
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 108.162.195.228


Name       : elliott.ns.cloudflare.com
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 162.159.44.228


Name       : elliott.ns.cloudflare.com
QueryType  : A
TTL        : 172800
Section    : Additional
IP4Address : 172.64.35.228


Name       : elliott.ns.cloudflare.com
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2606:4700:58::a29f:2ce4


Name       : elliott.ns.cloudflare.com
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2803:f800:50::6ca2:c3e4


Name       : elliott.ns.cloudflare.com
QueryType  : AAAA
TTL        : 172800
Section    : Additional
IP6Address : 2a06:98c1:50::ac40:23e4
```

```powershell
Resolve-DnsName example.com -Type A -Server 108.162.192.162 -NoRecursion -TcpOnly -DnsOnly
```

```text
Name                                           Type   TTL   Section    IPAddress
....                                           ....   ...   .......    .........
example.com                                    A      300   Answer     172.66.147.243
example.com                                    A      300   Answer     104.20.23.154
```

```powershell
Resolve-DnsName example.com -Type A
```

```text
Name                                           Type   TTL   Section    IPAddress
....                                           ....   ...   .......    .........
example.com                                    A      105   Answer     104.20.23.154
example.com                                    A      105   Answer     172.66.147.243
```

_Answer: The root referred me to the com servers, and the com server referred me to Cloudflare. The UDP query to the com server failed in PowerShell, but the TCP retry worked. The authoritative server at 108.162.192.162 returned a TTL of 300 seconds, while my normal resolver returned 105. The com delegation TTL was 172800 seconds, or two days. I used the Windows commands, so I did not run dig +trace._

**What it showed me:** the three referrals (root → `com` → the domain's own
servers), which server finally answered, the TTL it gave compared with what
my normal resolver shows for the same name, and how long the `com`
delegation is cached.

## Two things to account for

1. **`+trace` that stops after one line.** If you leave out `@1.1.1.1`, some
   ISP resolvers refuse the non-recursive root query `+trace` starts with,
   and you get *"Received 28 bytes from …"* and nothing else. That's your
   resolver's policy, not a broken internet. Note whether it happened to you.
2. **A TTL that doesn't match.** The authoritative server always gives the
   full TTL; your resolver gives what's *left* of it. If the two numbers in
   section 4 differ, you just saw a cache counting down.

<!--I learned how to read DNS records and follow a lookup to the server with the official answer.-->
