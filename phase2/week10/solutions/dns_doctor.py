"""Mini-project — dns-doctor.

Needs: pip install dnspython

A CLI that takes a name and answers the four questions behind every "is it
DNS?" ticket: what does it resolve to, according to whom, for how long, and
do they agree? Tasks 1, 2, 4, and 5 give you the building blocks — the
application's view vs DNS's view, honest timings, per-resolver TTLs, and
every failure shape named — and this project joins them into one tool.

  Section 1 — What your application gets: what socket.getaddrinfo() returns
  (what any program on this machine will actually connect to) and how long it
  took, plus whether the name is pinned in the hosts file — in which case DNS
  is not even being asked.

  Section 2 — The records: against the system resolver, follow the CNAME
  chain hop by hop with each TTL, then print A, AAAA, MX, TXT, and NS with
  their TTLs, or "(none)" when the name exists but has no record of that type.

  Section 3 — Do the resolvers agree? Ask the system resolver, 8.8.8.8, and
  1.1.1.1 for A records; print each one's addresses, TTL, and time; then a
  one-line verdict that tells a CDN's normal disagreement apart from a real
  fault. Every failure (NXDOMAIN, NODATA, SERVFAIL, timeout) is a row, never a
  traceback.

Section 2 is the DNS rung of the request-doctor you build in Week 20. See the
Phase 2 README (Graduation Projects) for the expected output format.
"""

# TODO: implement the mini-project.
print("dns-doctor — not implemented yet. Build your DNS diagnosis tool here!")
