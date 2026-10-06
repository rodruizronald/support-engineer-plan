# Weeks 7–8 — Answers: Processes, the Shell, and Program Launch

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The shell and how a program gets launched

### Q1. What is a shell (a program that reads a line, rewrites it, and launches other programs)? Walk the sequence from pressing Enter to a running process (parse → expand → resolve on `PATH` → fork → exec → wait). What's the difference between a builtin like `cd` and an external command like `ls`, and why can't `cd` be an external program?

_Your answer: A shell is a program that reads the commands we type, interprets them, and launches other programs. When I press Enter, the shell first parses the command to understand its structure. Then it performs expansions, such as replacing variables or expanding filename patterns. After that, it looks for the requested program using PATH. On Unix-like systems, the shell can use fork to create a child process and then exec to replace the child’s program with the program I asked to run. The shell can then wait for that child process to finish and collect its exit status._

_A builtin command such as cd is part of the shell itself, while an external command such as ls is normally a separate executable program. cd needs to be a builtin because it changes the current working directory of the shell itself. If cd were only an external program, it would run in a child process and could change that child’s directory, but when the child exited, the parent shell would still be in its original directory._

### Q2. What is `$PATH`, and how does the shell turn the name `python` into a file on disk? How do `which` / `command -v` report that, why does "command not found" almost always mean a PATH problem, and why must you write `./script.py` for a file in the current directory?

_Your answer: PATH is an environment variable that contains a list of directories where the shell looks for executable programs. When I type python, I usually do not give the shell the full path to the Python executable. Instead, the shell searches the directories listed in PATH in order until it finds a matching executable._

_Commands such as which python or command -v python can show which command or executable will be used. If I get “command not found,” a common reason is that the program is not installed or its directory is not included in PATH._

_The current directory is normally not searched automatically as part of PATH. That is why I may need to write ./script.py. The . means the current directory, so ./script.py explicitly tells the shell to use the file located there. The file also needs the appropriate permissions and, when executed directly as a script, normally an appropriate interpreter declaration such as a shebang._

### Q3. Explain the fork/exec model: what does `fork` duplicate and what does `exec` replace? Using Week 5's PID/PPID, describe the parent/child relationship, what it means for a parent to wait for (reap) a child, and what zombie and orphan processes are.

_Your answer: The fork/exec model explains how Unix-like systems commonly launch programs. fork creates a new child process based on the parent process. The parent and child have different PIDs, and the child’s PPID identifies its parent. After the fork, the child can use exec to replace the program it is currently running with another program. exec does not create another process; it replaces what the existing process is executing._

_When the child finishes, it leaves an exit status for its parent. The parent can wait for the child and collect that status, which is called reaping the child._

_A zombie process is a child that has already finished but whose parent has not yet collected its exit status, so the kernel keeps a small amount of information about it. An orphan process is different: it is still running, but its original parent has already terminated. The operating system then reparents it to an appropriate system process._

### Q4. Who expands what? Explain word splitting, globbing (`*.txt`), variable expansion (`$HOME`), and quoting (`'` vs `"`). Why does `python script.py *.txt` mean the *shell* produced that file list, and why does a file named `my report.pdf` break a careless script? Why does all this make passing untrusted text to a shell a command injection vulnerability, and what does the attacker get to do?

_Your answer: The shell performs several transformations before launching a program. Word splitting can divide certain unquoted expansion results into separate arguments. Globbing, or filename expansion, turns patterns such as *.txt into matching filenames. Variable expansion replaces expressions such as $HOME with their values._

_Quoting controls these interpretations. In Bash, single quotes '...' keep their contents literal, while double quotes "..." still allow expansions such as $HOME but protect the result from word splitting and filename expansion._

_For example, with python script.py *.txt, the shell normally expands *.txt before Python starts. If a.txt and b.txt exist, Python receives those filenames as arguments. Python did not create that file list; the shell did._

_A filename such as my report.pdf must be handled as one argument. Quoting it as "my report.pdf" prevents the space from being treated as an argument separator in the command._

_This also creates a security concern. If untrusted text is placed inside a command that a shell will interpret, special shell syntax in that input may be treated as instructions instead of data. This can lead to command injection, where an attacker causes unintended operating-system commands to run with the permissions of the vulnerable process._

### Q5. What are stdin, stdout, and stderr, and what are their file descriptor numbers (Week 5)? Explain redirection (`>`, `>>`, `2>`, `2>&1`, `<`) and what a pipe (`|`) connects to what. Why put results on stdout and errors on stderr — and why does `cmd > out.log` still show errors on screen?

_Your answer: stdin, stdout, and stderr are the three standard streams normally available to a process. Their file descriptor numbers are 0 for stdin, 1 for stdout, and 2 for stderr. stdin is normally used for input, stdout for normal program results, and stderr for errors and diagnostic messages._

_The shell can redirect these streams. > redirects stdout to a file and normally replaces the file’s previous contents, while >> appends stdout to the end of a file. 2> redirects stderr. 2>&1 makes file descriptor 2 go to the same destination as file descriptor 1 in that redirection context. < makes stdin come from a file._

_A pipe | connects the stdout of one command to the stdin of another command. This lets programs work together without needing an intermediate file._

_Keeping normal results on stdout and errors on stderr is useful because they can be handled separately. That is why cmd > out.log can still show errors on the screen: only stdout was redirected to the file, while stderr is still connected to the terminal._

## Part B — Doing it from Python

### Q6. What is `sys.argv`, and what's in `sys.argv[0]`? Given Q4, what has the shell already done to your command line before Python sees it — so what does `sys.argv` contain when you run `myscript.py *.txt "two words"`? Why is `argparse` a better habit than indexing `sys.argv` by hand?

_Your answer: sys.argv is a Python list containing the command-line arguments passed to a script. sys.argv[0] normally contains the name or path used to invoke the script, and the remaining elements contain its arguments._

_Before Python receives these arguments, the shell has already performed the shell expansions that apply. For example, if I run myscript.py *.txt "two words" and the directory contains a.txt and b.txt, the script may receive arguments equivalent to ["myscript.py", "a.txt", "b.txt", "two words"]. The shell expanded *.txt, while the quotes kept "two words" together as one argument._

_For very small scripts, I can read positions from sys.argv manually, but argparse is a better habit for real command-line tools. It can define required and optional arguments, validate values, convert types, generate usage information, and automatically provide helpful --help output._

### Q7. Compare `subprocess.run(["ls", "-l"])` with `subprocess.run("ls -l", shell=True)`: who parses the command in each case, and which is safe with untrusted input? Explain `capture_output=True`, `text=True`, `check=True`, `timeout=`, and what's in `.returncode` / `.stdout` / `.stderr`. When is `shell=True` legitimate?

_Your answer: With subprocess.run(["ls", "-l"]), Python passes the program and its arguments directly without asking a shell to parse a command string. With subprocess.run("ls -l", shell=True), Python launches a shell and gives the command string to that shell for interpretation._

_The list form is generally safer when any arguments contain untrusted input because the input is passed as an argument instead of being interpreted as shell syntax. shell=True can create a command injection risk if untrusted text is inserted into the command._

_capture-output=True captures the child’s stdout and stderr. text=True returns captured output as strings instead of bytes. check=True raises CalledProcessError when the child exits with a non-zero status. timeout= limits how long Python waits for the process._

_The returned result has .returncode, and when output is captured it can also provide .stdout and .stderr._

_shell=True can be legitimate when I intentionally need shell features such as shell pipelines, redirections, or other shell syntax and the command is carefully controlled. It should not be used just to make command construction easier when untrusted input is involved._

### Q8. How does the shell chain commands with `&&` and `||`, and why can a deploy script without `set -e` continue past a failed step and still report success? How do you make your own Python tool a good citizen — meaningful exit codes via `sys.exit()`, errors on stderr, and `check=True` when calling children?

_Your answer:The shell uses exit statuses to decide how && and || behave. With command1 && command2, the second command runs only if the first succeeds. With command1 || command2, the second command runs if the first fails._

_A deployment script can be dangerous if it ignores failed commands. Without appropriate error handling, a command may return a non-zero exit status and the script can continue running later commands. It might eventually print a success message even though an earlier step failed. set -e is commonly used to make a shell script exit on certain failed commands, although its exact behavior has important rules and exceptions._

_A Python CLI tool should also communicate success and failure clearly. It can use sys.exit(0) for success and meaningful non-zero exit codes for errors. Diagnostic and error messages should go to stderr instead of normal stdout. When Python launches child processes, check=True is useful when a failed child should cause the parent to handle that failure instead of silently continuing._

### Q9. How does a child process get its environment, and how do you give a child a different one (`env=`) without changing your own? Then: why does output appear instantly in a terminal but arrive late — or vanish on a crash — when piped or redirected? Explain line-buffered vs block-buffered stdout (Week 6), and the three fixes (`flush=True`, `python -u`, `PYTHONUNBUFFERED=1`).

_Your answer:A child process normally receives an environment based on the environment provided by its parent. In Python, I can create a copy with os.environ.copy(), change values in that copy, and pass it to a child with the env= argument. This gives the child a different environment without changing the parent process’s own environment._

_Output buffering explains why output can behave differently depending on its destination. When stdout is connected to an interactive terminal, output is commonly handled in a way that makes complete lines appear quickly. When stdout is redirected to a file or pipe, larger buffering may be used for efficiency. As a result, output can remain in a buffer for some time before another process sees it._

_If the process crashes or is force-killed while data is still buffered in user space, some output may never be written._

_In Python, flush=True can force a print() call to flush its output. Running Python with python -u enables unbuffered behavior for the standard streams, and setting PYTHONUNBUFFERED=1 provides another way to request that behavior. These options are especially useful for services, containers, and logs where output needs to appear promptly._

### Q10. (Capstone — all of Phase 1.) You type `python analyze.py data.csv | grep ERROR > out.txt` and press Enter. Trace every layer: what the shell parses and expands, how `python` is resolved on PATH, the fork/exec, the pipe and redirection as file descriptors (Week 5), the read of `data.csv` (Week 6), the bytes and decoding (Week 2), the objects in RAM (Week 3), the four components doing the work (Week 1), and the exit codes travelling back. Then name one realistic way each layer can fail.

_Your answer: When I type python analyze.py data.csv | grep ERROR > out.txt, the shell first parses the command. It recognizes two commands connected by a pipe and a redirection of the second command’s stdout to out.txt. It also performs any applicable expansions before launching the programs._

_The shell resolves python and grep, using PATH when necessary, and creates the processes needed to run them using the fork/exec model. It also creates a pipe. The stdout file descriptor of the Python process is connected to the writing side of the pipe, while the stdin of grep is connected to the reading side. The stdout of grep is redirected to out.txt._

_Python then runs analyze.py. When the script opens data.csv, it asks the operating system to resolve the path, check permissions, open the file, and provide access through a file descriptor. The data ultimately comes from storage, although the OS page cache may already contain some of it._

_At the data level, the file contains bytes. If Python opens it in text mode, those bytes are decoded using an encoding and become Python strings. Those strings and any lists, dictionaries, or other objects created by the program live in the process’s virtual memory and use RAM while they are active._

_The Week 1 components are all connected to this process: the CPU executes instructions, RAM holds active program data, disk stores the programs, input file, and output file, and the network interface would participate if the program needed network communication._

_The Python program writes results to stdout, but because stdout is connected to the pipe, those results become input for grep. grep looks for matching ERROR lines and writes its results to stdout, which the shell redirected to out.txt._

_Finally, the processes terminate and return exit statuses that their parents or the shell can collect._

_A realistic failure can happen at every layer: the shell command can have incorrect syntax or quoting; python or grep may not be found on PATH; process creation can fail because of resource limits; permissions can prevent execution or file access; data.csv may not exist; the disk may fill while writing out.txt; decoding may fail because of an incorrect encoding; loading too much data can exhaust memory; a pipe can be closed unexpectedly; or the program itself can contain a bug. The exit status then helps communicate whether each program succeeded or failed._
