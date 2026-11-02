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

_Paste output here._

**What it showed me:** _which record types came back and which didn't (look
for the AAAA line), who handles this company's email, and how many different
DNS providers serve the zone._

## 2. A CNAME chain

```
$ dig +noall +answer www.microsoft.com
```

_Paste output here._

**What it showed me:** _how many aliases sit between the name I asked for and
an address, whose name the address finally belongs to, and what happens to
the TTL at each hop._

## 3. Reverse DNS

```
$ dig +short -x 8.8.8.8
```

_Paste output here._

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

_Paste output here._

**What it showed me:** _the three referrals (root → `com` → the domain's own
servers), which server finally answered, the TTL it gave compared with what
my normal resolver shows for the same name, and how long the `com`
delegation is cached._

## Two things to account for

1. **`+trace` that stops after one line.** If you leave out `@1.1.1.1`, some
   ISP resolvers refuse the non-recursive root query `+trace` starts with,
   and you get *"Received 28 bytes from …"* and nothing else. That's your
   resolver's policy, not a broken internet. Note whether it happened to you.
2. **A TTL that doesn't match.** The authoritative server always gives the
   full TTL; your resolver gives what's *left* of it. If the two numbers in
   section 4 differ, you just saw a cache counting down.
