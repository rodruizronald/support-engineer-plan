# Week 5 — Answers: The Operating System as Middleman

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The OS and what it manages

### Q1. What is an operating system, and what does "the OS is a middleman between your program and the hardware" mean? Give two things your program can't do on its own and must ask the OS to do.

_Your answer:_

### Q2. User space vs kernel space, and the system call: what's the difference, why does the divide exist, and roughly what happens when your code calls `open()` — how does the request cross into the kernel and back?

_Your answer:_

### Q3. What is a process? What does the OS track about each one (PID, parent, memory, open files, state)? How is a process different from a program (the file on disk) and from a thread?

_Your answer:_

### Q4. A CPU has few cores, yet hundreds of processes seem to run at once. How does the scheduler create that illusion (time-slicing, context switches)? What is load average really measuring, and what does a load average well above your core count tell you?

_Your answer:_

### Q5. What is virtual memory, and why does each process act as if it owns all of RAM? What does the OS do when physical RAM runs out (paging/swapping — tie to Week 1's latency), and what is the OOM killer?

_Your answer:_

## Part B — How Python and your shell show you this

### Q6. How do you read your own PID and parent PID from Python (`os.getpid()`, `os.getppid()`) and your environment variables (`os.environ`)? Why do services get config and secrets from the environment instead of hard-coding them?

_Your answer:_

### Q7. What is a file descriptor? When you `open()` a file or socket, what does the OS hand back, and why do long-running services hit "Too many open files"? How does the `with` statement tie in, and what is a descriptor leak?

_Your answer:_

### Q8. What is a signal? Explain SIGINT (Ctrl-C), SIGTERM, and SIGKILL. What's the difference between a graceful shutdown and being force-killed, why does `kill -9` skip your cleanup, and how do you catch a signal in Python?

_Your answer:_

### Q9. What is an exit code? What do 0 and non-zero mean, and how does the shell read the last one with `$?`? How do you set an exit code from Python (`sys.exit`) and read a child's exit code? (Bonus: why is a SIGKILLed container's exit code 137?)

_Your answer:_

### Q10. (Tie-back to Weeks 1–3.) Objects (Week 3) live in a process's virtual memory, are made of bytes (Week 2), and sit in RAM the OS hands out across the four components (Week 1). Walk through what the OS does from pressing Enter on `python script.py` to the process exiting — and where the OS steps in to read a file or when memory runs out.

_Your answer:_
