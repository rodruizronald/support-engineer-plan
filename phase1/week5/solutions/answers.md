# Week 5 — Answers: The Operating System as Middleman

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The OS and what it manages

### Q1. What is an operating system, and what does "the OS is a middleman between your program and the hardware" mean? Give two things your program can't do on its own and must ask the OS to do.

_Your answer:An operating system is the software that manages a computer's hardware and resources and allows programs to use them safely. It acts as a middleman because programs do not directly control the hardware. Instead, they ask the operating system to perform certain operations for them. For example, a program needs the OS to open or read a file from disk and to obtain memory in RAM. The operating system manages these resources and returns the result to the program._

### Q2. User space vs kernel space, and the system call: what's the difference, why does the divide exist, and roughly what happens when your code calls `open()` — how does the request cross into the kernel and back?

_Your answer:User space is where normal programs such as Python, VS Code, or a web browser run with limited privileges to protect the system. Kernel space is where the kernel runs. The kernel is the core of the operating system and has the privileges needed to manage memory, processes, files, and hardware. This separation prevents a program from directly damaging the system or interfering with other programs._
_When our code calls open(), the program does not access the disk directly. It makes a system call to ask the kernel to open the file. The kernel checks the request and permissions, performs the operation, and returns the result to the program in user space._

### Q3. What is a process? What does the OS track about each one (PID, parent, memory, open files, state)? How is a process different from a program (the file on disk) and from a thread?

_Your answer:A process is an instance of a program that is currently running. The operating system keeps information about each process, including its PID (a number that identifies it), its parent process, the memory it uses, its open files, and its current state._
_A program is simply a file containing instructions stored on disk, while a process is that program while it is running. A thread is a unit of execution inside a process. A process can have one or more threads that share the process's memory and other resources._

### Q4. A CPU has few cores, yet hundreds of processes seem to run at once. How does the scheduler create that illusion (time-slicing, context switches)? What is load average really measuring, and what does a load average well above your core count tell you?

_Your answer:A CPU may have only a few cores even though hundreds of processes are active. The operating system's scheduler decides which process can use each CPU core and for how long. Through time-slicing, processes receive small turns of CPU time. A context switch happens when the CPU saves the state of one process and switches to another. Because these switches happen very quickly, many processes appear to run at the same time._
_Load average roughly indicates how many tasks are running or waiting for system execution resources (and on Linux it can also include tasks in uninterruptible waits, such as some I/O). If the load average stays well above the number of CPU cores, there is more work waiting than the CPU can handle immediately, which can indicate an overloaded system._

### Q5. What is virtual memory, and why does each process act as if it owns all of RAM? What does the OS do when physical RAM runs out (paging/swapping — tie to Week 1's latency), and what is the OOM killer?

_Your answer:Virtual memory is a system that gives each process its own virtual address space, making it appear to have separate memory for itself. The operating system maps these virtual addresses to real locations in physical memory and keeps processes isolated from one another._
_When physical RAM starts running out, the operating system may move memory pages between RAM and storage through mechanisms such as paging and swapping. As we learned in Week 1, accessing disk is much slower than accessing RAM, so excessive swapping can make the system very slow. If the system can no longer satisfy memory demands, systems such as Linux may use the OOM killer (Out Of Memory killer) to terminate one or more processes and free memory._

## Part B — How Python and your shell show you this

### Q6. How do you read your own PID and parent PID from Python (`os.getpid()`, `os.getppid()`) and your environment variables (`os.environ`)? Why do services get config and secrets from the environment instead of hard-coding them?

_Your answer:In Python, we can get our process's PID using os.getpid() and its parent PID using os.getppid(). We can also access environment variables through os.environ._
_Environment variables allow configuration and sensitive values, such as keys or credentials, to be provided to a program without writing them directly into the source code. This makes configuration easier to change between environments and helps prevent secrets from being accidentally stored in source code or a Git repository. However, environment variables still need to be handled carefully because they are not automatically a secure secret store._

### Q7. What is a file descriptor? When you `open()` a file or socket, what does the OS hand back, and why do long-running services hit "Too many open files"? How does the `with` statement tie in, and what is a descriptor leak?

_Your answer:A file descriptor is an identifier that the operating system uses to represent a resource opened by a process, such as a file or socket. When a program opens one of these resources, the operating system keeps the information needed to access it, and the process works with an associated descriptor._
_Each process has a limit on how many descriptors it can keep open. If a long-running service keeps opening files or connections without closing them, it can reach that limit and receive a "Too many open files" error. This is called a descriptor leak. In Python, using with helps prevent this because it automatically closes the file when we are finished with it, even if an exception occurs._

### Q8. What is a signal? Explain SIGINT (Ctrl-C), SIGTERM, and SIGKILL. What's the difference between a graceful shutdown and being force-killed, why does `kill -9` skip your cleanup, and how do you catch a signal in Python?

_Your answer:A signal is a way for the operating system to notify a process that something happened or request that it take an action. SIGINT is normally sent when we press Ctrl-C and requests that the program be interrupted. SIGTERM asks a process to terminate and gives it an opportunity to perform cleanup before exiting. SIGKILL terminates the process immediately and cannot be caught or ignored by the process._
_A graceful shutdown allows a program to close files and connections and release resources before exiting. In contrast, kill -9 sends SIGKILL, so the process has no opportunity to run its cleanup code. In Python, catchable signals can be handled with the signal module by registering a function to run when the signal arrives._

### Q9. What is an exit code? What do 0 and non-zero mean, and how does the shell read the last one with `$?`? How do you set an exit code from Python (`sys.exit`) and read a child's exit code? (Bonus: why is a SIGKILLed container's exit code 137?)

_Your answer:An exit code is a number returned by a process when it finishes to indicate whether it succeeded or encountered a problem. Usually, 0 means the program completed successfully, while a non-zero value indicates an error or another special condition_

_In shells such as Bash, we can check the previous command's exit code with $?. In Python, we can set an exit code using sys.exit(number), and when a program starts another process, it can read the exit code returned by that child process. As a bonus, a container terminated by SIGKILL commonly reports exit code 137 because of the convention 128 + signal number; SIGKILL is signal 9, so 128 + 9 = 137._

### Q10. (Tie-back to Weeks 1–3.) Objects (Week 3) live in a process's virtual memory, are made of bytes (Week 2), and sit in RAM the OS hands out across the four components (Week 1). Walk through what the OS does from pressing Enter on `python script.py` to the process exiting — and where the OS steps in to read a file or when memory runs out.

_Your answer:When we type python script.py and press Enter, the shell asks the operating system to start Python as a new process. The OS creates and tracks the process, gives it a PID and a virtual memory space, and the scheduler gives it CPU time to run. Python reads script.py and begins executing its instructions._

_The objects Python creates are made of bytes and live inside the process's memory, which ultimately uses physical RAM managed by the operating system. When the program needs to read a file, it asks the operating system to open it, and the kernel performs the operations needed to obtain the data. If the process needs more memory, the OS manages and allocates available memory; under memory pressure it may use paging or swapping, and if memory becomes critically exhausted, the system may terminate processes, for example through the OOM killer on Linux. Finally, when the program finishes, it returns an exit code and the operating system releases the process's resources._
