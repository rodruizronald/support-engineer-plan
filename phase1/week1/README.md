## Module 1 — Week 1: The Four Components and Their Speeds

### Weekly Objective

Understand the four physical components of a modern computer (CPU, RAM, disk, network interface), internalize the **latency hierarchy** that explains nearly every performance problem in software, and see — in your own running Python code — where a program's data lives and why some operations are millions of times slower than others.

### Brief Context

A computer is not a magic black box. It is four kinds of hardware that move data between each other at wildly different speeds. The **CPU** performs calculations. **RAM** is short-term, fast working memory that disappears when power is lost. **Disk** (SSD or HDD) is long-term storage that survives a reboot but is far slower than RAM. The **network interface** (Wi-Fi or Ethernet) connects this machine to others.

The single most important fact in computing is that these four components have speeds that differ by *orders of magnitude*: a CPU register access takes ~1 nanosecond, RAM ~100 nanoseconds, an SSD ~100 microseconds, a network round trip ~10–100 milliseconds. Almost every performance problem you will ever debug is some version of "data accidentally crossed a slow boundary too many times."

This week you build that picture from the bottom up. First you learn what the hardware *is*. Then you connect it to what your own Python program is actually doing — where a variable lives, what survives a reboot, what "out of memory" means. Finally you look at the same facts through a support engineer's eyes: when someone says "the app is slow," what do you suspect, and what do you check first?

> **How to work through the week:** Answer the research questions in your own words first (write them in `solutions/answers.md`), then do the practical tasks, then build the mini-project — your scripts for both live in `solutions/`. Theory loads the mental model; the code locks it in.

### Research Questions

Answer each in your own words in `solutions/answers.md`. Don't copy-paste definitions — explain them as if to a friend.

#### Part A — The hardware itself

1. A computer is often described as four components: CPU, RAM, disk, and network interface. In one sentence each, what is the single job of each one?
2. What does a CPU physically do, and what does a clock speed like 3.2 GHz actually count? Why does a higher number not always mean a faster computer?
3. RAM and disk both store data — so why does a computer need *both* instead of just one? What does each one give up in exchange for being good at its job?
4. RAM is described as "volatile." What does that mean, and what happens to everything in RAM the moment the power is cut?
5. What is physically different between an SSD and an HDD, and which one is in the machine you're using right now? (You'll confirm your guess with code in Task 7.)
6. The **latency hierarchy** ranks how long it takes to reach data in different places. Order these from fastest to slowest and note the rough order of magnitude for each: CPU register, L1 cache, RAM, SSD, HDD, network round trip inside one data center, network round trip across the internet. Why is it worth carrying these rough numbers in your head?

#### Part B — How a Python program uses that hardware

7. When you type `python script.py` and press enter, walk through which of the four components get involved, and in what rough order, to get your code running and printing output.
8. When your script runs `x = 5`, where does the value `5` physically live while the program is running? What about a list of a million numbers — where does *that* live, and roughly how much room does it take?
9. What happens to `x` when the script finishes, or when the machine reboots? If you needed that value to still be there tomorrow, what would you have to do, and which component would it have to live on?
10. Reading a 1 GB file from disk takes far longer than looping over a list of the same size that's already in RAM. Using what you learned about the latency hierarchy, explain *why*.
11. People say a program "ran out of memory." What is actually filling up? What is the operating system forced to do when it happens, and why might it kill the program?
12. A single network request (fetching a web page, say) can take longer than *millions* of CPU operations. In terms of the four components, what is your program actually *waiting on* during that request?

#### Part C — The support engineer's lens

13. In your own words, what does a support engineer do day-to-day? Why would knowing how CPU, RAM, and disk behave help someone debug a production problem in code they didn't write?
14. A user reports "the app is slow." Using only the latency hierarchy, list the categories of likely cause, ordered from most to least likely, and say what makes each one plausible.
15. When a support engineer first logs into a struggling machine, they almost always want to see its CPU load, free RAM, and free disk space immediately. Why are those three numbers the first thing to check? (You'll build a tool that prints them in the mini-project.)

### Practical Tasks

Each task is a separate, tiny Python file (think 5–20 lines). Run each one, look at the output, and write one sentence in your notes about what it showed you. Each task practices something from the questions above.

1. **Task 1 — Run your first script.** *(Practices Q7.)* Print a greeting and your name, then run it from the terminal with `python hello.py`. Goal: Python installed, editor open, a script running. **Concepts:** running a `.py` file, the `print()` function.
2. **Task 2 — Look at where a variable lives.** *(Practices Q8.)* Set `x = 5`, then print `id(x)` (an identifier tied to its location in memory) and `sys.getsizeof(x)` (how many bytes it occupies). Repeat for a huge integer and for a string, and notice the byte counts change. **Concepts:** `import`, variables, `id()`, `sys.getsizeof()`.
3. **Task 3 — Survive a reboot.** *(Practices Q9.)* Write a script that remembers how many times it has been run: on the first run it writes `1` to a file; on every later run it reads the number, adds one, and writes it back. Close your editor, even reboot — the count persists because it lives on disk, not in RAM. **Concepts:** `open()`, the `with` statement, `.read()` / `.write()`, `int()` / `str()`.
4. **Task 4 — Time a tight loop.** *(Practices Q2.)* Use `time.perf_counter()` to measure a `for` loop running a few million trivial iterations (e.g., `total += 1`). Print the total time and the average time per iteration. **Concepts:** `time.perf_counter()`, `for` loops, f-strings.
5. **Task 5 — Time a disk read against a memory loop.** *(Practices Q10.)* Read a small text file many times in a loop and time it; compare against the in-memory loop from Task 4. See for yourself that touching disk is slower. **Concepts:** reusing `open()`/`with`, comparing two timed measurements.
6. **Task 6 — Time a network request.** *(Practices Q12.)* Use `urllib.request.urlopen()` to fetch a public URL once and print how long it took, wrapped in `try`/`except` so a dropped connection doesn't crash the script. **Concepts:** importing from a submodule, `try`/`except`, calling a function that returns an object.
7. **Task 7 — Ask the machine about itself.** *(Practices Q5 and Q15.)* Install `psutil` (`pip install psutil`) and use it plus `platform` to print your CPU core count, total and free RAM, free disk space, and OS name. Confirm your SSD-vs-HDD guess from Q5. **Concepts:** `pip install`, third-party libraries, reading values off an object.
8. **Task 8 — Build the slowdown table.** *(Practices Q6 and Q14.)* Take the timings from Tasks 4–6, store them in variables, find the fastest, and print a small table with a column showing how many times slower each operation is than that fastest one. **Concepts:** storing values in variables, arithmetic, formatted printing (column alignment).

### Mini-Project: `health-snapshot`

A small CLI tool that does two things a support engineer does in the first minute of triaging a slow machine: **report what the box is**, and **show where time goes**. Tasks 7 and 8 are the two halves — this project joins them into one tool with a clean report.

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

A note on honesty: a single memory operation (~50 ns) is far too fast to time on its own from Python — the interpreter overhead alone is bigger. So you measure the *total* time over millions of iterations and divide to get an honest **average**. Your numbers will differ from the example, and on different runs — that variation is itself part of the lesson, not a bug.

The point is not perfect benchmarking. The point is to *see* the latency hierarchy printed by your own code, about your own laptop. This becomes the first artifact in your GitHub portfolio — and the embryo of every "why is the server slow?" investigation you'll do later.

**If you want to push further (optional):** add a flag like `--watch` that reprints the machine section every few seconds, or save each run's results to a file so you can compare snapshots over time.
