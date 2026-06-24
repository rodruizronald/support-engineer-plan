# Week 1 — Answers: The Four Components and Their Speeds

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The hardware itself

### Q1. The four components (CPU, RAM, disk, network interface) — one sentence on each one's single job.

- **CPU:** _The CPU executes instructions and performs calculations._
- **RAM:**_RAM is temporary memory that stores data while a program is running._
- **Disk:**_The disk stores data permanently, even when the computer is turned of._
- **Network interface:**_The network interface sends and receives data between computers. It allows Wi-Fi, Internet, and Ethernet connections._

### Q2. What does a CPU physically do, and what does a clock speed like 3.2 GHz count? Why is a higher number not always faster?

_Your answer: The CPU follows intructions, processes infromation and performs calculations. A clock speed of 3.2GHz means the CPU can performs about 3.2 billion cycles per second. A higher number is not always faster because different CPUs can do different amounts of work in each cycle._

### Q3. Why does a computer need both RAM and disk instead of just one? What does each give up in exchange for being good at its job?

_Your answer: RAM is very fast, but it is temporary memory. The disk is slower, but it keeps data permanently. One provides speed and the other one provides storage._

### Q4. RAM is "volatile." What does that mean, and what happens to everything in RAM the moment power is cut?

_Your answer: It means that RAM needs power to keep data. When the power is cut, everything stored in RAM disappears._

### Q5. Order these fastest → slowest with rough orders of magnitude: CPU register, L1 cache, RAM, SSD, HDD, network round trip in one data center, network round trip across the internet. Why carry these numbers in your head?

_Your answer: It is important to know this order because it helps explain why some operations are much slower than others._

## Part B — How a Python program uses that hardware

### Q6. When you run `python script.py`, which of the four components get involved, and in what rough order?

_Your answer: The program is stored on the disk, loaded into RAM, and then executed by the CPU. The network interface only participates if the program needs internet access or communicates with another computer._

### Q7. When your script runs `x = 5`, where does the value live while the program runs? What about a list of a million numbers?

_Your answer: The value lives in RAM while the program is running. A list of a million numbers also lives in RAM, but it uses much more memory_

### Q8. What happens to `x` when the script finishes or the machine reboots? How would you make the value survive, and where would it have to live?

_Your answer: The value disappears from RAM when the script finishes or the computer restarts. To keep it, it must be saved to a file or another storage device on disk._

### Q9. Why does reading a 1 GB file from disk take far longer than looping over a list of the same size already in RAM?

_Your answer: Because the disk is slower than RAM. Data already in RAM can be accessed quickly, while data on disk must first be read and copied into RAM, which takes more time._

### Q10. A single network request can take longer than millions of CPU operations. In terms of the components, what is your program waiting on?

_Your answer: The program is waiting for data to travel through the network and for the remote computer to send back a response._
