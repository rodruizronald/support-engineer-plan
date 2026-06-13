# Week 1 — Answers: The Four Components and Their Speeds

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The hardware itself

### Q1. The four components (CPU, RAM, disk, network interface) — one sentence on each one's single job.

- **CPU:**
- **RAM:**
- **Disk:**
- **Network interface:**

### Q2. What does a CPU physically do, and what does a clock speed like 3.2 GHz count? Why is a higher number not always faster?

_Your answer:_

### Q3. Why does a computer need both RAM and disk instead of just one? What does each give up in exchange for being good at its job?

_Your answer:_

### Q4. RAM is "volatile." What does that mean, and what happens to everything in RAM the moment power is cut?

_Your answer:_

### Q5. What is physically different between an SSD and an HDD, and which one is in your machine?

_Your answer:_

### Q6. Order these fastest → slowest with rough orders of magnitude: CPU register, L1 cache, RAM, SSD, HDD, network round trip in one data center, network round trip across the internet. Why carry these numbers in your head?

_Your answer:_

## Part B — How a Python program uses that hardware

### Q7. When you run `python script.py`, which of the four components get involved, and in what rough order?

_Your answer:_

### Q8. When your script runs `x = 5`, where does the value live while the program runs? What about a list of a million numbers?

_Your answer:_

### Q9. What happens to `x` when the script finishes or the machine reboots? How would you make the value survive, and where would it have to live?

_Your answer:_

### Q10. Why does reading a 1 GB file from disk take far longer than looping over a list of the same size already in RAM?

_Your answer:_

### Q11. When a program "runs out of memory," what is filling up? What is the OS forced to do, and why might it kill the program?

_Your answer:_

### Q12. A single network request can take longer than millions of CPU operations. In terms of the components, what is your program waiting on?

_Your answer:_

## Part C — The support engineer's lens

### Q13. What does a support engineer do day-to-day, and why does knowing how CPU, RAM, and disk behave help debug code you didn't write?

_Your answer:_

### Q14. A user reports "the app is slow." Using only the latency hierarchy, list likely causes most → least likely, and why each is plausible.

_Your answer:_

### Q15. Why are CPU load, free RAM, and free disk space the first three numbers a support engineer checks on a struggling machine?

_Your answer:_
