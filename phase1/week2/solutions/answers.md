# Week 2 — Answers: Binary, Bytes, and How Data Is Represented

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — Bits, bytes, and the number bases

### Q1. What is a bit and what is a byte? Why is a byte 8 bits, and how many distinct values can one byte represent?

_Your answer:_

### Q2. What does the "base" of a number system mean? Explain binary, decimal, and hex. Why do programmers lean on hex, and why does one byte fit in exactly two hex digits?

_Your answer:_

### Q3. How is a whole number stored in a fixed number of bits? Signed vs unsigned, and what is overflow / wraparound? Give a real example of a counter or timestamp that overflowed.

_Your answer:_

### Q4. How does a computer store "A", "é", and an emoji? Explain ASCII vs Unicode vs an encoding like UTF-8. Why is one character not the same as one byte?

_Your answer:_

### Q5. KB vs KiB (and MB vs MiB): why does a "1 TB" drive show as ~931 GB? Bits vs bytes: why does a "100 Mbps" connection download at ~12 MB/s?

_Your answer:_

## Part B — How Python represents that data

### Q6. In Python, what's the difference between a `str` and a `bytes`? When you save text to a file or send it over a network, which one travels, and what step converts between them?

_Your answer:_

### Q7. What is a `UnicodeDecodeError`, and in terms of encodings what has gone wrong? Why can the same file open fine in one program and show mojibake in another?

_Your answer:_

### Q8. Why does `0.1 + 0.2` not equal `0.3`? In terms of bits, what can't a float represent exactly, and why should you never store money as a float?

_Your answer:_

### Q9. Where have you seen hex (pick two: memory addresses, color codes, bytes in a log, error codes)? What do the digits mean there, and how do you convert a hex string to a number and back?

_Your answer:_

### Q10. (Tie-back to Week 1.) A 4-byte integer and a 1000-character UTF-8 string both live in RAM and may hit disk or the network. Using the latency hierarchy, why does knowing the byte size of your data matter for all three components?

_Your answer:_
