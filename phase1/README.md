# Phase 1 — Hardware Fundamentals Through Python (Weeks 1–8)

The detailed plan for Phase 1 of the Support Engineer learning journey.

## Goal of This Phase

Build the operator's mental model of the machine. Not the designer's, not the computer scientist's — the operator's. A SaaS or backend support engineer does not need to design CPUs, but they do need to know why a service runs out of memory, why disk I/O is slow, why a process gets killed, and what the operating system is actually doing underneath the application code. Phase 1 builds that intuition by pairing every concept with a Python experiment the learner runs on their own machine.

By the end of Phase 1, the learner should be able to answer in their own words: what physically happens when a program runs, where a variable lives, why memory and disk behave so differently, what a process is, and what role the operating system plays as the middleman between code and hardware.

## How Each Week Works

Every sub-phase (one per week) follows the same shape:

1. **Weekly Objective.** One sentence stating what this week is targeting.
2. **Brief Context.** A short paragraph framing the topic. Just enough to orient, not a tutorial.
3. **Research Questions.** A set of questions the learner answers by researching online (documentation, articles, Stack Overflow, official docs) and writes up in their own words. Answers go in that week's `solutions/answers.md`.
4. **Practical Tasks.** Several small standalone Python tasks, each focused on one concept. Each task is intentionally tiny (5–20 lines of code) so the learner can digest one idea at a time.
5. **Graduation Project.** One small but functional Python program that ties the week's tasks together into something real — not a contrived exercise, but a tool the learner could imagine actually using. Each week offers a menu of project options; the learner picks one and builds it. Completing one project per week is how the learner passes Phase 1 — see [Graduation Projects](#graduation-projects) below.

The research happens *before* the practical part each week. Theory loads the mental model; practice locks it in.

Each week lives in its own folder (e.g., `week1/`): the plan in `README.md`, and the learner's work — research answers in `solutions/answers.md` plus a Python script per task and the chosen graduation project — in the `solutions/` subfolder.

## The 6 Sub-Phases

1. **Week 1:** [The Four Components and Their Speeds](week1/README.md).
2. **Week 2:** [Binary, Bytes, and How Data Is Represented](week2/README.md).
3. **Weeks 3–4:** Memory, Variables, and What Python Is Actually Doing.
4. **Week 5:** The Operating System as Middleman.
5. **Week 6:** Files, Paths, and I/O.
6. **Weeks 7–8:** Processes, the Shell, and Program Launch.

## Graduation Projects

Each sub-phase ends with a mini-project: a small but functional Python program that ties that week's tasks together into something real — not a contrived exercise, but a tool you could imagine actually using. Each week offers a **menu** of project options; you pick one and build it.

**To pass Phase 1, complete one project for each of the six sub-phases.** By the end you'll have a portfolio of small tools — each one demonstrating a different layer of the machine — and proof that you can *apply* what you learned, not just answer questions about it.

Projects are added here as each week is developed. So far Weeks 1 and 2 are available; more weeks, and more options per week, will be filled in over time.

### Week 1 — The Four Components and Their Speeds

Pick one project to build. (More options will be added here over time — for now there is one.)

#### Option A — `health-snapshot`

A small CLI tool that does two things a support engineer does in the first minute of triaging a slow machine: **report what the box is**, and **show where time goes**. Tasks 3, 4, and 5 give you the building blocks — the memory/disk/network timings and the machine report — and this project joins them into one tool, adding a slowdown table that compares the speeds.

**Section 1 — This machine.** Using `psutil`, `platform`, and `shutil`, print the CPU core count, total/free RAM, free disk space, and the OS.

**Section 2 — Where time goes.** Run three measurements — an in-memory loop, a small disk read, and a single real network request — and print a table with the average time per operation and a "slowdown vs the fastest" column.

Output should look roughly like:

```
=== This machine ===
CPU      : 8 cores
RAM      : 16.0 GB total, 6.2 GB free
Disk     : 120 GB free
OS       : macOS 25.4

=== Where time goes ===
Operation        Avg time      Slowdown vs memory
Memory loop      ~0.05 us/op   1x
Disk read        ~5 us/op      ~100x
Network (GET)    ~45 ms/op     ~900,000x
```

A note on honesty: a single memory operation (~50 ns) is far too fast to time on its own from Python — the interpreter overhead alone is bigger. So you measure the *total* time over millions of iterations and divide to get an honest **average**. Your numbers will differ from the example, and from run to run — that variation is itself part of the lesson, not a bug.

A skeleton is provided at `week1/solutions/health_snapshot.py`. The point is not perfect benchmarking; it's to *see* the latency hierarchy printed by your own code, about your own laptop. This becomes the first artifact in your GitHub portfolio — and the embryo of every "why is the server slow?" investigation you'll do later.

**If you want to push further (optional):** add a `--watch` flag that reprints the machine section every few seconds, or save each run's results to a file so you can compare snapshots over time.

### Week 2 — Binary, Bytes, and How Data Is Represented

Pick one project to build. (More options will be added here over time — for now there is one.)

#### Option A — `encoding-doctor`

A small CLI tool that does what a support engineer does when a file shows up full of garbled characters: **look at the bytes and figure out how to read them.** Given a string (or a small file), it x-rays the data three ways. Tasks 1, 2, 3, and 6 give you the building blocks — number bases, characters-as-bytes, the encode/decode round-trip, and the hex dump — and this project joins them into one diagnostic tool.

**Section 1 — What is this data.** Report the number of characters vs the number of bytes when encoded as UTF-8, whether every character is plain ASCII, and flag any non-ASCII characters with their Unicode code point. (Bonus, tying back to Q5: print the byte count in both KB and KiB so the units difference is concrete.)

**Section 2 — Hex view.** Print a hexdump-style view of the first 16 bytes — an offset, the bytes as two hex digits each, and an ASCII gutter where printable characters show themselves and everything else shows as `.`.

**Section 3 — Encoding sanity check.** Try decoding the bytes as ASCII, latin-1, and UTF-8, and report which succeed and which raise — so you can *see* why the same bytes look fine in one tool and garbled in another.

Output should look roughly like:

```
=== What is this data ===
Input    : "café 😀"
Chars    : 6
Bytes    : 10  (UTF-8)        0.010 KB / 0.0098 KiB
ASCII    : no
Non-ASCII: 'é' U+00E9, '😀' U+1F600

=== Hex view (first 16 bytes) ===
00000000  63 61 66 c3 a9 20 f0 9f 98 80                    caf.. ....

=== Encoding sanity check ===
ascii    : FAILED  — 'ascii' codec can't decode byte 0xc3 in position 3
latin-1  : ok       — "cafÃ© ð\x9f\x98\x80"  (decodes, but wrong — mojibake)
utf-8    : ok       — "café 😀"  (correct)
```

A note on what you're seeing: latin-1 *never* fails to decode — it maps all 256 byte values to characters — which is exactly why it produces silent garbage instead of an error. UTF-8 is stricter, so it either gives you the right text or tells you the bytes aren't valid UTF-8. That contrast is the whole lesson of the week, printed by your own code.

A skeleton is provided at `week2/solutions/encoding_doctor.py`. The point isn't to reimplement `chardet`; it's to *see*, on data you choose, that bytes are just bytes until an encoding gives them meaning. This is the tool you'll mentally reach for every time a ticket says "the characters are all messed up."

**If you want to push further (optional):** accept a real file path on the command line, auto-suggest the most likely encoding, or add a `--bytes N` flag to control how much of the hex view to print.