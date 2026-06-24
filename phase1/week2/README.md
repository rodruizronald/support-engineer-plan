## Module 2 — Week 2: Binary, Bytes, and How Data Is Represented

### Weekly Objective

Internalize that everything a computer stores — numbers, text, colors, whole files — is ultimately just **bits grouped into bytes**, and that meaning only appears when you decide *how to read* those bytes. Learn the three number bases you'll meet every day (binary, decimal, hexadecimal), and see — in your own running Python code — why text needs an *encoding*, why `0.1 + 0.2` isn't `0.3`, and why a "1 TB" drive never shows 1000 GB.

### Brief Context

Underneath every program there are only **bits**: tiny on/off switches, each a 0 or a 1. Group eight of them and you get a **byte**, which can hold one of 256 distinct values. That's the whole alphabet the hardware has. Numbers, letters, emoji, pixels, machine code — all of it is bytes. The catch is that a byte by itself means *nothing*. The single byte `0x41` is the number 65, the letter `A`, or part of a color, depending entirely on how a program chooses to interpret it. An **encoding** is just an agreed-upon rule for that interpretation.

Almost every "the characters look garbled" bug and every "the number is slightly wrong" bug comes from a disagreement about how to read bytes — one program wrote them meaning one thing, another read them meaning something else. Support engineers see these constantly: a CSV full of `Ã©` where `é` should be, a financial report that's off by a penny, a "100 Mbps" link that downloads at 12 MB/s, a log line full of hex you need to decode. None of it is mysterious once you can see the bytes underneath.

This week you build that x-ray vision. First you learn what bits, bytes, and the number bases actually are. Then you connect it to what Python is doing — the difference between a `str` and a `bytes`, where encoding errors come from, and why floating-point math is fuzzy. By the end you should be able to look at raw bytes and reason about every layer stacked on top of them.

> **How to work through the week:** Answer the research questions in your own words first (write them in `solutions/answers.md`), then do the practical tasks (one script each, in `solutions/`). When you're ready, build this week's **graduation project** — see [Phase 1 → Graduation Projects](../README.md#graduation-projects). Theory loads the mental model; the code locks it in.

### Research Questions

Answer each in your own words in `solutions/answers.md`. Don't copy-paste definitions — explain them as if to a friend.

#### Part A — Bits, bytes, and the number bases

1. What is a **bit**, and what is a **byte**? Why is a byte 8 bits, and how many distinct values can a single byte represent? (Say where the number comes from.)
2. What does the "base" of a number system mean? Explain binary (base 2), decimal (base 10), and hexadecimal (base 16). The machine only speaks binary — so why do programmers lean so heavily on **hex**, and why does exactly one byte fit in two hex digits?
3. How is a whole number stored in a fixed number of bits (say 8, 16, 32, or 64)? What's the difference between **signed** and **unsigned**, and what happens when you try to store a number too big to fit — i.e. what is **overflow / wraparound**? Give a real example of a counter or timestamp that overflowed.
4. Text isn't numbers — so how does a computer store the letter `A`, the letter `é`, and an emoji like `😀`? Explain the difference between **ASCII**, **Unicode**, and an **encoding** like **UTF-8**. Why is "one character" *not* the same thing as "one byte"?
5. Storage and speed both come in confusing units. Explain **KB vs KiB** (and MB vs MiB): why does a "1 TB" drive show up as roughly 931 GB? And explain **bits vs bytes**: why does a "100 Mbps" internet connection only download at about 12 MB/s?

#### Part B — How Python represents that data

6. In Python, what's the difference between a `str` and a `bytes` object? When you save text to a file or send it over a network, which of the two actually travels down the wire or onto the disk, and what step converts a `str` into that form (and back)?
7. What is a `UnicodeDecodeError`, and in terms of encodings, what has actually gone *wrong* when you hit one? Why can the **same file** open perfectly in one program and show garbled "mojibake" in another?
8. Why does `0.1 + 0.2` not equal `0.3` in Python (and in almost every language)? In terms of bits, what is it that a floating-point number cannot represent exactly — and why should you never store money in a `float`?
9. Hex shows up everywhere an operator looks: memory addresses, color codes like `#FF8800`, individual bytes in a log or a hex dump, error and status codes. Pick **two** places you've actually seen hex and explain what the digits mean there. How would you convert a hex string to a number and back, both in your head and in Python?
10. *(Tie-back to Week 1.)* A 4-byte integer and a 1000-character UTF-8 string both have to live in RAM, and either one might get written to disk or sent across the network. Using the latency hierarchy from Week 1, explain why knowing the **byte size** of your data matters for all three of those components.

### Practical Tasks

Each task is a separate, tiny Python file (think 5–20 lines). Run each one, look at the output, and write one sentence in your notes about what it showed you. Each task practices something from the questions above. **Task 6 is optional** — a stretch for when you want to go further.

1. **Task 1 — See one number wear three outfits.** *(Practices Q1 and Q2.)* Take a number like `255`, then print it in binary, decimal, and hex, and convert back the other way. Use `bin()`, `hex()`, `int("ff", 16)`, `int("11111111", 2)`, and format specs like `f"{n:08b}"` and `f"{n:#x}"`. Goal: watch a single value look completely different in each base while staying the same number. **Concepts:** `bin()`, `hex()`, `int(string, base)`, format specifiers.
2. **Task 2 — A letter is a number is a byte.** *(Practices Q4.)* Take the character `"A"`, get its code point with `ord()`, turn a number back into a character with `chr()`, then `.encode()` a short string to `bytes` and print the raw byte values. See for yourself that `"A"` is `65` is `0x41`. **Concepts:** `ord()`, `chr()`, `str.encode()`, indexing a `bytes` object.
3. **Task 3 — Break an encoding, then fix it.** *(Practices Q6 and Q7.)* Take a string with a non-ASCII character (`"café"` or `"naïve 😀"`), `.encode()` it as UTF-8, then deliberately try to `.decode()` those bytes as ASCII and catch the `UnicodeDecodeError`. Then decode them correctly as UTF-8. Watch mojibake happen and then get fixed. **Concepts:** `.encode()` / `.decode()`, `try` / `except UnicodeDecodeError`, encoding names.
4. **Task 4 — Make an integer overflow on purpose.** *(Practices Q3.)* Python integers never overflow, so *simulate* a fixed-width unsigned 8-bit counter: start at 250, keep adding 1, and wrap every result with `% 256` (or mask it with `& 0xFF`). Print the value as it climbs past 255 and snaps back to 0. This is what languages like C do silently. **Concepts:** modulo `%`, bitwise AND `&`, hex literals, loops.
5. **Task 5 — Prove floating point is fuzzy.** *(Practices Q8.)* Print `0.1 + 0.2`, show it isn't `0.3`, then print the result with many decimals using `f"{x:.20f}"` to see the tiny error. Show the *right* way to compare floats (`math.isclose`) and the right way to handle money (`decimal.Decimal`). **Concepts:** float formatting, `math.isclose()`, `decimal.Decimal`.
6. **Task 6 — Build a tiny hex dump.** *(Optional — practices Q2 and Q9.)* Take a short string (or read a few bytes from a small file), and for each byte print its value as two hex digits next to the character it represents if it's printable — the same idea as the left columns of `xxd` or `hexdump`. **Concepts:** iterating over a `bytes` object, `f"{b:02x}"`, `chr()`, `str.isprintable()`.
