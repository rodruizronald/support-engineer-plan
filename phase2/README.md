# Phase 2 — Networking, HTTP, APIs, JSON (Weeks 9–20)

The detailed plan for Phase 2 of the Support Engineer learning journey.

## Goal of This Phase

Build the operator's mental model of a **request**. Phase 1 ended with one machine: hardware, the OS as middleman, files, and processes. Almost nothing in production is one machine. A ticket that says "the integration is broken" is really a claim about a request that left one process, crossed a name lookup, a route, a connection, a TLS handshake, a proxy, and a server's application code — and came back wrong, late, or not at all. A support engineer's core skill is isolating *which* of those layers failed, and proving it with evidence rather than a guess.

So Phase 2 is not "learn HTTP." It is: build the request/response model from the wire upward, one layer at a time, and end up with a **repeatable diagnostic ladder** — DNS → TCP → TLS → HTTP → auth → payload → application — where each rung has a question, a command that answers it, and a Python experiment that made it real.

By the end of Phase 2, the learner should be able to answer in their own words: what physically happens between typing a URL and seeing a response, what a "connection" actually is, why the same request succeeds in `curl` and fails in the browser (or the reverse), what a certificate proves, where a payload stops being bytes and becomes an object, which credential is being presented and when it expires, and — given a failure — which layer to blame and how to show it.

## What "Done" Looks Like

Concretely, by Week 20 the learner can:

- Take a hostname and prove, at each level, how it resolves — and explain a stale answer.
- Distinguish **connection refused**, **timeout**, and **connection reset** on sight, and say what each one implicates.
- Type a raw HTTP request into a socket by hand, and read a response without a library's help.
- Read a status code and headers and say whether the client, a proxy, or the server is at fault.
- Diagnose the five common TLS failures (expired, hostname mismatch, missing intermediate, self-signed, version/cipher mismatch) — and explain why `curl -k` "fixing" it is a finding, not a fix.
- Write a Python client that behaves well in production: timeouts, bounded retries, connection reuse, streaming, and error messages that name the layer.
- Navigate an unfamiliar API from its docs: pagination to completion, rate limits respected, errors handled.
- Reproduce a customer's request faithfully from a HAR file or a screenshot, with secrets stripped.

## Why the Wire Comes First

HTTP does not appear until Week 13. That is deliberate, and it is the same bet Phase 1 made by spending two weeks on hardware and bytes before writing much Python: **HTTP failures are mostly not HTTP failures.** "504 Gateway Timeout" is a TCP and topology story. "SSL: CERTIFICATE_VERIFY_FAILED" is a trust-chain story. "It works on my laptop, not in the container" is usually a DNS story. A learner who meets HTTP first has no place to put any of those, and ends up pattern-matching on error strings.

Weeks 9–12 exist so that when HTTP arrives, every layer beneath it is already something the learner has inspected with their own hands. The tools follow the same logic: `curl` shows up in Week 13 when there is finally a protocol worth aiming it at, `jq` in Week 16 when there is a payload worth filtering, and Week 20 consolidates the whole toolkit into one procedure.

## How Each Week Works

Every sub-phase (one module per week) follows the same shape as Phase 1:

1. **Weekly Objective.** One sentence stating what this week is targeting.
2. **Brief Context.** A short paragraph framing the topic. Just enough to orient, not a tutorial.
3. **Research Questions.** A set of questions the learner answers by researching online (RFCs where they're readable, official docs, articles, Stack Overflow) and writes up in their own words. Answers go in that week's `solutions/answers.md`.
4. **Practical Tasks.** Several small standalone tasks, each focused on one concept and intentionally tiny so the learner can digest one idea at a time.
5. **Graduation Project.** One small but functional program that ties the week's tasks together into something real — a tool the learner could imagine actually reaching for during a ticket. Each week offers a menu of options; the learner picks one and builds it. Completing one project per sub-phase is how the learner passes Phase 2 — see [Graduation Projects](#graduation-projects) below.

The research happens *before* the practical part each week. Theory loads the mental model; practice locks it in.

Each week lives in its own folder (`week9/` through `week20/`): the plan in `README.md`, and the learner's work in the `solutions/` subfolder — research answers in `solutions/answers.md`, plus one artifact per task and the chosen graduation project.

### Three things that are new in Phase 2

**Tasks are not always Python.** Half of this phase's muscle memory is command-line: `dig`, `curl`, `openssl s_client`, `jq`. A task that is genuinely a shell task stays a shell task — the artifact is then `solutions/taskN_<name>.md` holding the exact command, its real output, and two or three sentences on what the output proved. Python scripts (`solutions/taskN_<name>.py`) remain the default everywhere else, and several weeks deliberately do the same thing both ways so the learner sees that `curl` and `requests` are two handles on one protocol.

**The learner runs the server, not just the client.** Every week from 11 onward has a local target — a socket server, `python -m http.server`, or a tiny Flask app — because half of support work is reasoning about what the *other* side saw. Failures are induced on purpose (kill the server mid-response, point at a closed port, serve an expired certificate) instead of waited for.

**Every task produces evidence.** The output of a phase-2 task is not "it worked" — it is a request, a response, and a timing you could paste into a ticket. This is the habit Phase 5 later formalizes into bug reports and post-mortems, and it starts here.

## Practice Targets and Setup

**One-time setup.** Command line: `curl`, `dig`, `openssl`, `nc`, `traceroute`, `lsof` (mostly preinstalled on macOS), plus `jq` (`brew install jq`) and optionally `mtr` and `mitmproxy`. Python: `requests` (Week 17), plus a minimal server framework such as `flask` (Week 11 onward); `psutil` carries over from Phase 1.

**Targets, in order of preference.** (1) **Local servers the learner runs** — the only safe place to induce failures, and the default for Weeks 11–16. (2) **Public echo services** — `httpbin.org`, `postman-echo.com` — for status codes, redirects, headers, and auth schemes on demand. (3) **One real API, used across Weeks 17–19** — the GitHub REST API is the recommended choice: it is free, read-only-safe, documented, and it exercises pagination, rate limits with real headers, conditional requests with ETags, and token auth, so the same API keeps paying off for three weeks.

**Rules of engagement.** Probe only machines the learner owns and endpoints published as test targets — no port scanning or load testing anything else. Keep request volume low enough that no target notices. Real tokens live in environment variables, never in a file in the repo; anything pasted into `answers.md` gets redacted first. These are the same rules that apply on the job, so they are worth practicing now.

## The 11 Sub-Phases

1. **Week 9:** [The Network as Hardware — Packets, Addresses, and Ports](week9/README.md).
2. **Week 10:** DNS — Turning Names Into Addresses.
3. **Weeks 11–12:** TCP and Sockets — What a Connection Actually Is.
4. **Week 13:** HTTP/1.1 by Hand — The Plain-Text Protocol.
5. **Week 14:** HTTP Semantics — Methods, Status Codes, Headers, and Redirects.
6. **Week 15:** HTTPS and TLS — Why a Connection Is Trusted (or Isn't).
7. **Week 16:** JSON and Data Interchange.
8. **Week 17:** Calling APIs From Python With `requests`.
9. **Week 18:** REST Conventions, Pagination, and Rate Limits.
10. **Week 19:** Authentication and Authorization.
11. **Week 20:** The Debugging Ladder — `curl`, `jq`, DevTools, End to End.

Modules are written and linked here as the learner reaches them, the same way Phase 1 was built out.

## Sub-Phase Detail

### Sub-Phase 1 — Week 9: The Network as Hardware

**Objective.** Understand the fourth component from Phase 1 Week 1 as real hardware with a queue at each end, and see that reaching another machine takes three separate things: an **address**, a **route**, and a **port**.

**Covers.**

- The NIC, MAC vs IP addressing, and packets as the unit that actually travels (MTU, fragmentation, loss, reordering).
- IPv4 and IPv6, CIDR and subnet masks, private ranges vs public addresses, NAT, the default gateway and the routing table, hops and TTL.
- The layer model (link / internet / transport / application) introduced as a *debugging* tool: the ladder every later week climbs.
- Ports as numbers the OS hands out — well-known vs ephemeral, `0.0.0.0` vs `127.0.0.1` vs a LAN address, and the fact that a socket is a Week 5 file descriptor.
- Latency vs bandwidth vs throughput, and where a real round trip lands on Week 1's latency hierarchy.

**Builds on.** Week 1 (the four components, latency hierarchy), Week 5 (the OS owns the hardware; file descriptors).

**Planned graduation artifact.** `net-snapshot` — reports this machine's interfaces, addresses, gateway, and listening ports, then times a round trip to a few hosts and places the results on the Week 1 latency table.

### Sub-Phase 2 — Week 10: DNS — Turning Names Into Addresses

**Objective.** Internalize name resolution as a **hierarchy of caches** that can be inspected at every level — and learn why "it's always DNS" is a cliché with real mechanics behind it.

**Covers.**

- The resolver chain: stub resolver → recursive resolver → root → TLD → authoritative, and who answers from cache at each step.
- Record types worth knowing (A, AAAA, CNAME, MX, TXT, NS, SOA, PTR) and what a CNAME chain does to debugging.
- TTLs and the layers that cache them (application process, OS, resolver, browser); why "DNS propagation" is really TTL expiry.
- Failure shapes: NXDOMAIN vs SERVFAIL vs no answer at all, negative caching, and the difference between "the name is wrong" and "the resolver is unreachable."
- Where resolution is configured and how it differs per environment: `/etc/hosts`, `resolv.conf`, search domains, split-horizon and internal-only names, DNS inside containers.

**Builds on.** Week 9 (addresses and ports), Week 6 (config files the OS reads on your behalf).

**Planned graduation artifact.** `dns-doctor` — resolves a name against the system resolver and two public ones, prints every record and TTL, follows CNAME chains, and flags disagreement between resolvers.

### Sub-Phase 3 — Weeks 11–12: TCP and Sockets — What a Connection Actually Is

Two weeks, one sub-phase: the protocol first, then the code that speaks it.

**Objective.** Understand a "connection" as agreed-upon state on two machines, and be able to tell the three connection failures apart — because each one points at a different team.

**Module 11 — TCP the protocol.** The three-way handshake and what it costs (against Week 1's latency numbers); sequence numbers, acknowledgements, retransmission, and ordering; flow control and windows, congestion control at intuition level; teardown with FIN vs an abrupt RST, `TIME_WAIT`, the listen backlog, keep-alive. TCP vs UDP and when each is the right tool. Connection states as seen in `netstat`/`lsof`. **The three failures** — *refused* (nothing listening: an immediate RST), *timeout* (packets going into a black hole: a firewall or a wrong route), *reset mid-flight* (something alive killed it) — plus why connection pooling exists at all.

**Module 12 — Sockets in Python.** `bind`/`listen`/`accept` on one side, `connect` on the other; blocking behavior and why **every socket gets a timeout**; the fact that TCP is a byte stream with no message boundaries, so framing (a length prefix or a delimiter) is the learner's problem; partial sends and short reads; `SO_REUSEADDR` and "Address already in use"; closing sockets as closing file descriptors; a one-connection-at-a-time server and what it means when the second client just waits.

**Builds on.** Week 9 (ports), Week 5 (file descriptors, signals — killing a server mid-connection), Week 1 (why a handshake is expensive).

**Planned graduation artifact.** `tcp-triage` — one project across both weeks: a local echo server plus a prober that connects to a host and port, classifies the outcome as refused / timeout / reset / connected, and reports the time spent resolving vs connecting.

### Sub-Phase 4 — Week 13: HTTP/1.1 by Hand — The Plain-Text Protocol

**Objective.** See that HTTP is just text sent over a Week 11 connection — and lose any sense that a request library is doing something mysterious.

**Covers.**

- The exact shape of a request and a response: request line, headers, blank line, body; status line, headers, body; CRLF and case-insensitive header names.
- The `Host` header and virtual hosting: why one IP serves a thousand sites, and why the address alone no longer identifies the server.
- How a receiver knows where the body ends — `Content-Length` vs `Transfer-Encoding: chunked` — and what a truncated response looks like.
- Persistent connections: why HTTP/1.1 keeps the socket open, and what that means for the handshake cost from Week 11.
- URL anatomy (scheme, host, port, path, query, fragment) and percent-encoding, tying back to Week 2's bytes-vs-characters.
- HTTP/1.1 vs HTTP/2 vs HTTP/3 in one pass: what changes on the wire and what stays identical in semantics.
- First contact with `curl -v`, immediately after typing the same request by hand, so the `>` and `<` lines are recognizable.

**Builds on.** Weeks 11–12 (a connection to write into), Week 2 (encoding, bytes vs text), Week 6 (streaming a body rather than reading it whole).

**Planned graduation artifact.** `raw-http-client` — performs a complete GET over a bare socket with no HTTP library: builds the request text, reads the response, splits headers from body, and honors `Content-Length`.

### Sub-Phase 5 — Week 14: HTTP Semantics — Methods, Status Codes, Headers, and Redirects

**Objective.** Read a request/response pair and say who is at fault — client, proxy, or server — before touching any code.

**Covers.**

- Methods and their contracts: safe, idempotent, cacheable — GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS — and why the contract decides whether a retry is safe.
- Status codes as a diagnostic language: 200/201/204; 301 vs 302 vs 307/308; 304; 400/401/403/404/405/409/410/422/429; 500 vs 502 vs 503 vs 504 — with the key insight that 502/504 means *the thing in front couldn't get an answer from the thing behind*.
- Headers that change behavior: `Content-Type`, `Accept`, `Content-Encoding`, `Cache-Control`/`ETag`/`If-None-Match`, `Location`, `Set-Cookie`, `Authorization`, `Retry-After`, `X-Forwarded-For`, and request/correlation IDs.
- Redirect chains and what they do to the method, the body, and the `Authorization` header.
- Who else is in the path — reverse proxies, load balancers, CDNs, API gateways — and what they add, strip, buffer, or time out.

**Builds on.** Week 13 (the message format), Week 10 (a redirect to a different host resolves again).

**Planned graduation artifact.** `http-explain` — issues a request, prints the full request/response exchange annotated, follows the redirect chain step by step, and translates the final status and headers into a plain-language verdict.

### Sub-Phase 6 — Week 15: HTTPS and TLS — Why a Connection Is Trusted (or Isn't)

**Objective.** Know precisely what TLS adds on top of TCP, and diagnose the handful of ways it breaks without reaching for `-k`.

**Covers.**

- What TLS provides — confidentiality, integrity, **identity** — and what it does not (it says nothing about authorization).
- The handshake at a debuggable level: ClientHello, version and cipher negotiation, the certificate, key exchange, session resumption — and the extra round trips it adds.
- Certificates: subject and SAN, issuer, the chain to a root in the trust store, and why a **missing intermediate** fails on a server but works in a browser that cached it.
- The five failures worth recognizing on sight: expired, hostname mismatch, self-signed, missing intermediate, version/cipher mismatch — plus client clock skew as the impostor among them.
- SNI, and why the certificate you get depends on the name you asked for.
- What `curl -k` and `verify=False` actually disable, why they turn an outage into a silent vulnerability, and how corporate MITM proxies and custom CA bundles (`certifi`, `REQUESTS_CA_BUNDLE`, `SSL_CERT_FILE`) produce the same error legitimately.

**Builds on.** Weeks 11–12 (TLS is a layer on a TCP connection), Week 6 (certificate and CA files on disk), Week 2 (base64/DER vs PEM as encodings of the same bytes).

**Planned graduation artifact.** `cert-check` — connects to a host, prints the presented chain with subject, SAN, issuer, and days-to-expiry, verifies the hostname, and names which of the five failures it found.

### Sub-Phase 7 — Week 16: JSON and Data Interchange

**Objective.** Treat a payload as a typed structure with an encoding — and be precise about where a "malformed JSON" ticket really comes from.

**Covers.**

- The JSON grammar and its six types; no comments, no trailing commas, always UTF-8; duplicate keys and key ordering.
- Python's `json` module: the type mapping in both directions, `dumps`/`loads`, `indent`, `sort_keys`, `ensure_ascii`, and `default=` for the objects that refuse to serialize (`datetime`, `Decimal`, `set`, `bytes`).
- Where numbers betray you: float precision from Week 2, integers beyond JavaScript's 2^53, and `NaN`/`Infinity` as non-standard extensions.
- Parse errors as evidence: what "Expecting value: line 1 column 1" almost always means (an HTML error page, an empty body, or a gzip stream), and why the `Content-Type` header is a claim rather than a fact.
- Traversing untrusted nested data safely: missing vs `null` vs falsy, `.get()` with defaults, and failing with a message that names the field.
- The neighbors a support engineer meets: form-encoded and multipart bodies, JSON Lines for streaming, plus CSV, YAML, and XML in brief.
- `jq` as the everyday instrument: selecting, filtering, mapping, and `-r` for output you can pipe.

**Builds on.** Week 2 (bytes, encodings, floats), Week 3 (a parsed payload is now objects in RAM), Week 6 (streaming NDJSON instead of loading a huge file).

**Planned graduation artifact.** `payload-doctor` — reads a JSON document (or an NDJSON stream) and reports its shape: keys and inferred types at each level, depth, array sizes, and every value that would not survive a round trip.

### Sub-Phase 8 — Week 17: Calling APIs From Python With `requests`

**Objective.** Make the requests from Weeks 13–15 in code that would survive production — and map every exception back to the layer that raised it.

**Covers.**

- The `requests` surface: `params` vs `data` vs `json` vs `files`; headers; `response.status_code`/`headers`/`text`/`content`/`json()`; `raise_for_status()`.
- **Timeouts always**, connect and read separately — and what a missing timeout does to a process that a Week 5 signal then has to kill.
- `Session`: connection reuse (the Week 11 handshake, paid once), persistent cookies, default headers.
- Retries done properly: bounded attempts, exponential backoff with jitter, and only for the status codes and methods Week 14 says are safe.
- Streaming responses so a large download stays flat in memory — Week 6's habit, arriving over the network.
- `verify`, client certificates, and proxies (Week 15); redirect control and `response.history` (Week 14).
- The error taxonomy that matters: `ConnectionError` vs `Timeout` vs `HTTPError` vs `JSONDecodeError`, each pointing at a different rung of the ladder.
- Logging a request usefully without leaking a credential; `urllib` and `httpx` in one paragraph each.

**Builds on.** Weeks 13–15 (the protocol being wrapped), Week 6 (streaming), Week 3 (response objects and their memory), Week 5 (a hung process).

**Planned graduation artifact.** `api-client` — a small, well-behaved client module plus CLI: session reuse, sane timeouts, bounded retries with backoff, and error messages that say which layer failed.

### Sub-Phase 9 — Week 18: REST Conventions, Pagination, and Rate Limits

**Objective.** Walk into an unfamiliar API with only its docs and know what to expect before the first request returns.

**Covers.**

- Resource-oriented design: collections vs items, nesting, and the method/status conventions from Week 14 now seen in the wild.
- Reading API documentation as a skill: OpenAPI/Swagger specs, request collections, and the gap between docs and behavior.
- Pagination styles — page/offset, limit/offset, cursor, `Link` headers — why cursors win on changing data, and how each one fails halfway through.
- Filtering, sorting, sparse fields, and expansion; consistent error envelopes and correlation IDs.
- Versioning and deprecation: in the URL vs in a header, and what a sunset notice means for a customer's integration.
- Rate limits for real: 429, `Retry-After`, `X-RateLimit-*`, token buckets, and what being a good client looks like in code.
- Idempotency keys, and long-running work as `202` + polling vs webhooks (delivery retries, duplicates, signature verification).
- Eventual consistency as a ticket: "I created it and the next GET said 404."
- The non-REST neighbors — GraphQL, gRPC, SOAP — in a paragraph each, so none of them is a surprise.

**Builds on.** Weeks 14 and 17 (semantics and a client to apply them from).

**Planned graduation artifact.** `paginate-all` — walks a paginated API to completion against the real target API, respects rate-limit headers, and can resume from where it stopped.

### Sub-Phase 10 — Week 19: Authentication and Authorization

**Objective.** For any request, be able to say exactly what credential is being presented, where it came from, when it expires — and what 401 versus 403 is really telling you.

**Covers.**

- Identity vs permission: 401 ("I don't know who you are") vs 403 ("I know, and no"), and why confusing them sends a ticket to the wrong team.
- HTTP Basic and why base64 is encoding, not protection; API keys — header vs query string, scoping, rotation.
- Bearer tokens and JWTs: the three parts, base64url, the claims that matter (`exp`, `iat`, `nbf`, `iss`, `aud`), the difference between decoding a token and verifying it, and clock skew as the cause of "it expired instantly."
- OAuth 2.0 as actually encountered: client credentials for machine-to-machine, authorization code with PKCE for users, refresh tokens, scopes and consent, and the token endpoint.
- Cookies and sessions: `Set-Cookie`, `HttpOnly`, `Secure`, `SameSite`, domain and path scoping — the mechanics behind "it logged me out again."
- The two browser-only failures support gets asked about: **CORS** (preflight `OPTIONS`, `Access-Control-Allow-*`, and why `curl` succeeding proves nothing) and CSRF.
- mTLS in brief (Week 15 in the other direction), and secrets hygiene: environment variables, nothing credential-shaped in git, redaction before anything is pasted into a ticket, and what never to ask a customer to send.

**Builds on.** Week 14 (status codes, `Authorization`), Week 15 (why any of this needs TLS), Week 17 (presenting credentials from code), Week 2 (base64 as encoding).

**Planned graduation artifact.** `token-inspect` — decodes and explains a token without trusting it (claims, issuer, audience, time remaining, skew warning), and fetches a fresh one via client credentials to show the full acquire-use-expire-refresh cycle.

### Sub-Phase 11 — Week 20: The Debugging Ladder — `curl`, `jq`, DevTools, End to End

**Objective.** Consolidate eleven weeks into one repeatable procedure that isolates any request failure to a single layer, with evidence attached. This is the phase capstone.

**Covers.**

- `curl` as the primary instrument: `-v`, `-i`, `-I`, `-X`, `-H`, `-d`/`--data-binary`, `-F`, `-L`, `-o`, `--compressed`, `-x`, `--resolve`, `--cert` — and `-w` with a timing format that prints `time_namelookup`, `time_connect`, `time_appconnect`, `time_starttransfer`, `time_total`: the entire ladder in one line of output.
- `jq` pipelines against real payloads, and the small set of expressions that covers most triage.
- Browser DevTools: the Network panel's waterfall and timing breakdown, request and response headers, initiator, preserve log, disable cache, throttling, and **Copy as cURL** — plus reading a HAR file a customer sent and understanding what it does and doesn't contain.
- An intercepting proxy (mitmproxy) in brief, for the cases where the client won't tell you what it sent.
- **The ladder itself**, as the deliverable: for each rung — DNS, TCP, TLS, HTTP, auth, payload, application — one question, one command that answers it, and what a pass or fail there rules out. Client vs network vs proxy vs server, decided by evidence.
- Reproducing a customer's request faithfully, and sanitizing it before it goes anywhere.
- Writing up a finding so the next person can act on it — a first pass at the bug-report shape Phase 5 formalizes.

**Builds on.** Everything in Phase 2, plus Week 5 (process and system state) and Week 6 (reading the log the server left behind).

**Planned graduation artifact (phase capstone).** `request-doctor` — takes a URL and walks the full ladder, printing a per-layer verdict and timing: resolution, connection, TLS chain, HTTP exchange, credential state, payload validity — and a one-line conclusion naming the layer that failed.

## Graduation Projects

Each sub-phase ends with a mini-project: a small but functional program that ties that sub-phase's tasks together into something real — not a contrived exercise, but a tool you could imagine actually reaching for mid-ticket. Each week offers a **menu** of options; you pick one and build it.

**To pass Phase 2, complete one project for each of the eleven sub-phases.** The Week 20 capstone, `request-doctor`, is the phase's headline artifact: by the time you build it, every layer it inspects is one you have already probed by hand, and most of its sections are earlier projects grown up. Phase 1 left you a portfolio of tools that each explain one layer of a machine; Phase 2 leaves you a diagnostic kit for the request — the single most common thing a support engineer is handed and asked to explain.

Projects are added here as each week is developed. So far Week 9 is available; more weeks, and more options per week, will be filled in over time.

### Week 9 — The Network as Hardware

Pick one project to build. (More options will be added here over time — for now there is one.)

#### Option A — `net-snapshot`

A small CLI tool that answers the first three questions a support engineer asks about a machine's place on the network: **what are its addresses**, **who is listening on it**, and **how far away is everything else.** Tasks 1, 2, 3, and 4 give you the building blocks — interfaces and MTUs, the private-vs-public address gap, bound ports and file descriptors, and honest round-trip timing — and this project joins them into one tool.

**Section 1 — This machine on the network.** Using `psutil` and `socket`, print the hostname, then one line per active interface with its IPv4 address and netmask, MAC, and MTU. Then the three facts that tell you where this machine actually sits: the **default gateway**, the **source address** the OS would use to reach the internet (the UDP-connect trick from Task 2), and the **public address** the internet sees. When the last two differ, you are looking at NAT.

**Section 2 — Who's listening here.** List every listening TCP port with the address it is bound to, and — the column that matters — whether that binding is **local-only** (`127.0.0.1`) or **reachable from the network** (`0.0.0.0`). This is the section that answers "the service is running but nothing can connect to it."

**Section 3 — Where the time goes.** TCP round trips to four targets at increasing distance — loopback, your gateway, a nearby host, a distant one — as min/avg/max, with a slowdown column against Week 1's memory figure and the cost of **20 sequential** round trips at that average.

Output should look roughly like:

```
=== This machine on the network ===
Hostname : Ronalds-MacBook-Pro.local
en0      : 192.168.1.24/24  mac 8c:85:90:1f:22:7d  mtu 1500   up
lo0      : 127.0.0.1/8      mac n/a                mtu 16384  up
Gateway  : 192.168.1.1  (via en0)
Source   : 192.168.1.24  (the address the OS picks to reach the internet)
Public   : 203.0.113.47  (what the internet sees — NAT in between)

=== Who's listening here ===
Address     Port   Reachable from           Process
127.0.0.1   8099   this machine only        python3.12 (pid 48213)
0.0.0.0     5000   anywhere on the network  python3.12 (pid 48310)
*             22   anywhere on the network  n/a (needs sudo)

=== Where the time goes ===
Target                 RTT min/avg/max        vs memory     20 in a row
loopback               0.09 / 0.11 / 0.14 ms      ~2,000x          2 ms
gateway 192.168.1.1     3.1 / 4.4 / 9.5 ms       ~88,000x         88 ms
example.com              74 / 78 / 86 ms      ~1,560,000x        1.56 s
```

A note on what you're seeing, and on honesty. Three of these choices are deliberate and worth understanding, because each one is a lesson:

- **Round trips are measured with a TCP connect, not with `ping`.** ICMP needs no privileges here, measures what an *application* actually experiences, and — critically — is not filtered the way ICMP so often is. A gateway that ignores every `ping` you send will still complete a TCP handshake and still answer as traceroute's first hop. "No ping reply" is not "down," and a tool that concluded otherwise would lie to you.
- **Names are resolved once, up front, and the timings connect to the IP.** Otherwise your first sample silently includes a DNS lookup and comes out two or three times too high. Week 10 times that lookup properly, as its own rung of the ladder.
- **Section 2 will not be complete without `sudo`, and should say so.** On macOS, `psutil.net_connections()` raises `AccessDenied` for a non-root process; falling back to `lsof -nP -iTCP -sTCP:LISTEN` shows you your *own* processes and nothing else. Print `n/a (needs sudo)` rather than an empty row or a guess — noticing which facts the OS will and won't hand over is the same lesson Week 5 taught with `num_fds()`.

Your numbers will differ from the example, and from run to run — on Wi-Fi, wildly. That variation is the network being honest, not a bug; it's also why the tool reports min/avg/max instead of a single number.

A skeleton is provided at `week9/solutions/net_snapshot.py`. The point isn't to reimplement `ifconfig` and `ping`; it's to *see*, for your own machine, the three facts that every later week depends on — which addresses it has, which ports are exposed, and what a round trip costs. This is the first artifact of Phase 2 in your portfolio, and it's the direct ancestor of the `request-doctor` you build in Week 20: Section 3 is that tool's bottom two rungs.

**If you want to push further (optional):** add a `--json` flag so two snapshots can be diffed (run it at home and at the office and compare), add a `--port N` check that reports whether a port is free *before* a service tries to bind it, or add a `--watch` flag that reprints Section 3 every few seconds so you can watch latency move while the network is busy.

## What Phase 2 Hands to Phase 3

Phase 3 moves from a laptop to running services on remote machines. It assumes exactly what this phase built: that a service is something reachable over an address and a port, that its failures arrive as status codes and timeouts, and that the way to find out what happened is to ask each layer in order. The log-reading habit from Week 6 meets the request IDs from Week 14; the socket from Week 12 becomes a service listening behind a reverse proxy; `curl` becomes the thing you run over SSH to ask a box about itself.
