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
3. **Weeks 3–4:** Memory, Variables, and What Python Is Actually Doing — [Week 3: Names, Objects, and References](week3/README.md).
4. **Week 5:** [The Operating System as Middleman](week5/README.md).
5. **Week 6:** [Files, Paths, and I/O](week6/README.md).
6. **Weeks 7–8:** Processes, the Shell, and Program Launch.

## Graduation Projects

Each sub-phase ends with a mini-project: a small but functional Python program that ties that week's tasks together into something real — not a contrived exercise, but a tool you could imagine actually using. Each week offers a **menu** of project options; you pick one and build it.

**To pass Phase 1, complete one project for each of the six sub-phases.** By the end you'll have a portfolio of small tools — each one demonstrating a different layer of the machine — and proof that you can *apply* what you learned, not just answer questions about it.

Projects are added here as each week is developed. So far Weeks 1, 2, 3, 5, and 6 are available; more weeks, and more options per week, will be filled in over time.

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

### Week 3 — Names, Objects, and References

Pick one project to build. (More options will be added here over time — for now there is one.)

#### Option A — `reference-detective`

A small CLI tool that answers the question behind a whole family of tickets: **"I only touched one thing — why did something else change?"** Given a few names you bind to objects, it x-rays how Python actually holds them. Tasks 1, 2, 3, and 5 give you the building blocks — aliasing, `is` vs `==`, mutate-vs-rebind, and shallow-vs-deep copy — and this project joins them into one diagnostic tool.

**Section 1 — Names & identity.** For each name, print its `id()` and refcount, then group the names that are **aliases** of the same object (same `id`) versus ones that are merely **equal but separate** (`==` is `True`, `is` is `False`).

**Section 2 — Mutation blast radius.** Mutate one shared object exactly once and report every name whose value changed as a side effect — the aliasing "blast radius" made visible. This is the literal answer to "why did my other variable change?"

**Section 3 — Copy comparison.** Take a nested structure, build a **shallow** copy and a **deep** copy, mutate a nested element in the original, and show which copy still shares it (changed) and which isolates it (unchanged) — proving a shallow copy only protects the top level.

Output should look roughly like:

```
=== Names & identity ===
Name    id            refs   group
a       0x10a3f2c40   3      shared #1  (aliases: a, b)
b       0x10a3f2c40   3      shared #1  (aliases: a, b)
c       0x10a3f2e80   2      unique

a == c ?  True    (equal contents)
a is c ?  False   (different objects)

=== Mutation blast radius ===
Mutating a.append(99) ...
Changed as a side effect : a, b   (they share one list)
Unaffected               : c      (a separate object)

=== Copy comparison ===
Original       : [[1, 2], [3, 4]]
Mutating original[0].append(99) ...
                shares nested?   value now
shallow copy    yes              [[1, 2, 99], [3, 4]]
deep copy       no               [[1, 2], [3, 4]]
```

A note on what you're seeing: the shallow copy is a brand-new *outer* list, so replacing a whole element in the original wouldn't touch it — but its inner lists are the *same objects* as the original's, so mutating one of those bleeds straight through. A deep copy rebuilds the objects all the way down, which is why it stays isolated (and why it costs more time and memory). That contrast is the whole lesson of the week, printed by your own code.

A skeleton is provided at `week3/solutions/reference_detective.py`. The point isn't to reimplement a debugger; it's to *see*, on names you choose, that assignment binds rather than copies — the reflex you'll reach for every time a ticket says "nothing else should have changed."

**If you want to push further (optional):** add a section that runs a small operation in a loop and reports whether an object's refcount keeps climbing (a mini leak detector), or take the structure to inspect from a small config so you can point it at different shapes.

### Week 5 — The Operating System as Middleman

Pick one project to build. (More options will be added here over time — for now there is one.)

#### Option A — `process-probe`

A small CLI tool that does what a support engineer does when triaging a misbehaving service: **point at a process and ask the OS everything about it.** Given a PID (defaulting to the tool's own process), it x-rays the process three ways. Tasks 1, 2, 3, and 6 give you the building blocks — process identity, the process table, file descriptors, and child processes — and this project joins them into one diagnostic tool.

**Section 1 — Identity & environment.** Using `os` and `psutil`, print the PID, the parent PID (and the parent's name), the process name, the user it runs as, its status, how long it has been running, and its working directory.

**Section 2 — Resources it holds.** Print the process's memory (RSS/VMS), CPU percent, thread count, and number of open file descriptors — its footprint on the four components from Week 1.

**Section 3 — In the context of this machine.** Print the overall system CPU percent, total/available RAM, and the load average, so you can see the one process against the whole box.

Output should look roughly like:

```
=== Identity ===
PID      : 48213
PPID     : 48090  (parent: zsh)
Name     : python3.12
User     : rodruizronald
Status   : running
Started  : 2026-07-21 09:14:02  (up 0:03:12)
CWD      : /Users/rodruizronald/workspace/private/support-engineer-plan

=== Resources it holds ===
Memory   : 18.4 MB RSS / 402.1 MB VMS
CPU      : 0.3%
Threads  : 3
Open FDs : 7

=== In the context of this machine ===
System CPU   : 12.5% busy
System RAM   : 16.0 GB total, 5.8 GB available
Load average : 2.10, 1.85, 1.60  (1m, 5m, 15m)
```

A note on portability: some of these fields are OS-specific. `psutil.Process().num_fds()` and `os.getloadavg()` work on macOS and Linux but not plain Windows, so wrap the ones that might not exist in `try`/`except` and print `n/a` when they're missing — noticing *which* facts the OS will and won't tell you is part of the lesson. Your numbers will differ from the example and from run to run; that variation is the machine being honest, not a bug.

A skeleton is provided at `week5/solutions/process_probe.py`. The point isn't to reimplement `top` or `ps`; it's to *see*, for a process you choose, the identity, resources, and context the OS is tracking on your behalf — the exact three questions you'll ask every time a ticket says "the service is using too much memory" or "the process won't die." This is the tool that turns Week 1's four components into something you can inspect live.

**If you want to push further (optional):** accept a PID on the command line so you can probe *other* processes, add a `--children` flag that lists the target's child processes, or add a `--watch` flag that reprints Section 2 every few seconds so you can watch memory climb in real time.

### Week 6 — Files, Paths, and I/O

Pick one project to build. (More options will be added here over time — for now there is one.)

#### Option A — `log-triage`

A small CLI tool that does what a support engineer does in the first minute with a log file: **figure out what the file is, find out what's in it without loading it into RAM, and read the end of it.** Given a path to a log file, it reports three things. Tasks 1, 2, 3, 4, and 5 give you the building blocks — text vs bytes, `pathlib`, streaming reads, metadata, and I/O errors — and this project joins them into one triage tool.

**Section 1 — What this file is.** Using `pathlib`, print the resolved absolute path, the size in both **MB and MiB** (Week 2's units difference, made concrete on a real file), the last modification time plus **how long ago** that was, and the permission bits.

**Section 2 — What's inside (streamed).** Scan the file one line at a time and report the total line count, a count per log level (ERROR / WARN / INFO / DEBUG), the first and last timestamp seen, and the **peak memory used while scanning** — proving you can scan a file far bigger than the RAM you spend on it.

**Section 3 — The last N lines.** Print a tail (default 10 lines). Keep it in a fixed-size `collections.deque(maxlen=N)` so memory stays flat no matter how big the file is.

Output should look roughly like:

```
=== What this file is ===
Path     : /Users/you/logs/app.log
Size     : 4.812 MB / 4.589 MiB
Modified : 2026-08-17 09:41:07  (3 minutes ago)
Mode     : 644

=== What's inside (streamed, never fully loaded) ===
Lines    : 48,201
ERROR    :    312
WARN     :  1,004
INFO     : 46,780
DEBUG    :    105
First ts : 2026-08-16 22:00:03
Last ts  : 2026-08-17 09:41:06
Peak RAM : 0.07 MB  (to scan a 4.8 MB file)

=== Last 10 lines ===
2026-08-17 09:40:58 INFO  request id=8821 status=200 in 43ms
...
2026-08-17 09:41:06 ERROR db connection refused (attempt 3/3)
```

A note on what you're seeing: the **Peak RAM** line is the whole point of the week. A `.read()` would have made that number roughly the size of the file; streaming line-by-line keeps it near zero, and the `deque` keeps the tail cheap too — so the same code works on a 5 MB log and a 5 GB one. Two other details worth getting right, because real logs are messier than test files: open the file with `errors="replace"` so one corrupt byte doesn't crash the whole scan with a `UnicodeDecodeError` (Week 2, arriving through `open()`), and wrap the open in `try`/`except` so a missing file or a permissions problem prints a clear message instead of a traceback.

If you don't have a log file handy, generate one first — a short loop that writes a few hundred thousand timestamped lines with random levels gives you something realistic to point the tool at, and it doubles as practice for Task 3.

A skeleton is provided at `week6/solutions/log_triage.py`. The point isn't to reimplement `tail` or `grep`; it's to *see* that you can answer real questions about a file bigger than your RAM by never holding more than one line of it at a time. This is the habit behind every "can you check the logs?" request you'll ever get, and it's the direct ancestor of the log work in Phase 3.

**If you want to push further (optional):** add a `--grep PATTERN` flag that prints only matching lines (still streaming), a `--follow` flag that behaves like `tail -f` by watching for new lines appended to the end, or a histogram showing how many lines fall in each hour so you can spot the moment things went wrong.