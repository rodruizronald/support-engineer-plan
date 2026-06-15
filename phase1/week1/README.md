## Module 1 — Week 1: The Four Components and Their Speeds

### Weekly Objective

Understand the four physical components of a modern computer (CPU, RAM, disk, network interface), internalize the **latency hierarchy** that explains nearly every performance problem in software, and see — in your own running Python code — where a program's data lives and why some operations are millions of times slower than others.

### Brief Context

A computer is not a magic black box. It is four kinds of hardware that move data between each other at wildly different speeds. The **CPU** performs calculations. **RAM** is short-term, fast working memory that disappears when power is lost. **Disk** (SSD or HDD) is long-term storage that survives a reboot but is far slower than RAM. The **network interface** (Wi-Fi or Ethernet) connects this machine to others.

The single most important fact in computing is that these four components have speeds that differ by *orders of magnitude*: a CPU register access takes ~1 nanosecond, RAM ~100 nanoseconds, an SSD ~100 microseconds, a network round trip ~10–100 milliseconds. Almost every performance problem you will ever debug is some version of "data accidentally crossed a slow boundary too many times."

This week you build that picture from the bottom up. First you learn what the hardware *is*. Then you connect it to what your own Python program is actually doing — where a variable lives and what survives a reboot.

> **How to work through the week:** Answer the research questions in your own words first (write them in `solutions/answers.md`), then do the practical tasks (one script each, in `solutions/`). When you're ready, build this week's **graduation project** — see [Phase 1 → Graduation Projects](../README.md#graduation-projects). Theory loads the mental model; the code locks it in.

### Research Questions

Answer each in your own words in `solutions/answers.md`. Don't copy-paste definitions — explain them as if to a friend.

#### Part A — The hardware itself

1. A computer is often described as four components: CPU, RAM, disk, and network interface. In one sentence each, what is the single job of each one?
2. What does a CPU physically do, and what does a clock speed like 3.2 GHz actually count? Why does a higher number not always mean a faster computer?
3. RAM and disk both store data — so why does a computer need *both* instead of just one? What does each one give up in exchange for being good at its job?
4. RAM is described as "volatile." What does that mean, and what happens to everything in RAM the moment the power is cut?
5. The **latency hierarchy** ranks how long it takes to reach data in different places. Order these from fastest to slowest and note the rough order of magnitude for each: CPU register, L1 cache, RAM, SSD, HDD, network round trip inside one data center, network round trip across the internet. Why is it worth carrying these rough numbers in your head?

#### Part B — How a Python program uses that hardware

6. When you type `python script.py` and press enter, walk through which of the four components get involved, and in what rough order, to get your code running and printing output.
7. When your script runs `x = 5`, where does the value `5` physically live while the program is running? What about a list of a million numbers — where does *that* live, and roughly how much room does it take?
8. What happens to `x` when the script finishes, or when the machine reboots? If you needed that value to still be there tomorrow, what would you have to do, and which component would it have to live on?
9. Reading a 1 GB file from disk takes far longer than looping over a list of the same size that's already in RAM. Using what you learned about the latency hierarchy, explain *why*.
10. A single network request (fetching a web page, say) can take longer than *millions* of CPU operations. In terms of the four components, what is your program actually *waiting on* during that request?

### Practical Tasks

Each task is a separate, tiny Python file (think 5–20 lines). Run each one, look at the output, and write one sentence in your notes about what it showed you. Each task practices something from the questions above. **Task 6 is optional** — a stretch for when you want to go further.

1. **Task 1 — Run your first script.** *(Practices Q6.)* Print a greeting and your name, then run it from the terminal with `python task1_hello.py`. Goal: Python installed, editor open, a script running. **Concepts:** running a `.py` file, the `print()` function.
2. **Task 2 — Survive a reboot.** *(Practices Q8.)* Write a script that remembers how many times it has been run: on the first run it writes `1` to a file; on every later run it reads the number, adds one, and writes it back. Close your editor, even reboot — the count persists because it lives on disk, not in RAM. **Concepts:** `open()`, the `with` statement, `.read()` / `.write()`, `int()` / `str()`.
3. **Task 3 — Time memory against disk.** *(Practices Q2 and Q9.)* Use `time.perf_counter()` to measure two things and compare them: a `for` loop running a few million trivial iterations (pure RAM/CPU work), and reading a small text file many times in a loop (touches the disk). See for yourself how much slower the disk is. **Concepts:** `time.perf_counter()`, `for` loops, `open()`/`with`, f-strings.
4. **Task 4 — Time a network request.** *(Practices Q10.)* Use `urllib.request.urlopen()` to fetch a public URL once and print how long it took, wrapped in `try`/`except` so a dropped connection doesn't crash the script. Compare it to your memory and disk timings from Task 3. **Concepts:** importing from a submodule, `try`/`except`, calling a function that returns an object.
5. **Task 5 — Ask the machine about itself.** *(Practices Q1.)* Install `psutil` (`pip install psutil`) and use it plus `platform` to print three of the four components as they exist on your own machine — CPU core count, total/free RAM, free disk space — plus the OS. **Concepts:** `pip install`, third-party libraries, reading values off an object.
6. **Task 6 — Look at where a variable lives.** *(Optional — practices Q7.)* Set `x = 5`, then print `id(x)` (an identifier tied to its location in memory) and `sys.getsizeof(x)` (how many bytes it occupies). Repeat for a huge integer and for a string, and notice the byte counts change. **Concepts:** `import`, variables, `id()`, `sys.getsizeof()`.
