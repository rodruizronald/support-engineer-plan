# Weeks 7–8 — Answers: Processes, the Shell, and Program Launch

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — The shell and how a program gets launched

### Q1. What is a shell (a program that reads a line, rewrites it, and launches other programs)? Walk the sequence from pressing Enter to a running process (parse → expand → resolve on `PATH` → fork → exec → wait). What's the difference between a builtin like `cd` and an external command like `ls`, and why can't `cd` be an external program?

_Your answer:_

### Q2. What is `$PATH`, and how does the shell turn the name `python` into a file on disk? How do `which` / `command -v` report that, why does "command not found" almost always mean a PATH problem, and why must you write `./script.py` for a file in the current directory?

_Your answer:_

### Q3. Explain the fork/exec model: what does `fork` duplicate and what does `exec` replace? Using Week 5's PID/PPID, describe the parent/child relationship, what it means for a parent to wait for (reap) a child, and what zombie and orphan processes are.

_Your answer:_

### Q4. Who expands what? Explain word splitting, globbing (`*.txt`), variable expansion (`$HOME`), and quoting (`'` vs `"`). Why does `python script.py *.txt` mean the *shell* produced that file list, and why does a file named `my report.pdf` break a careless script? Why does all this make passing untrusted text to a shell a command injection vulnerability, and what does the attacker get to do?

_Your answer:_

### Q5. What are stdin, stdout, and stderr, and what are their file descriptor numbers (Week 5)? Explain redirection (`>`, `>>`, `2>`, `2>&1`, `<`) and what a pipe (`|`) connects to what. Why put results on stdout and errors on stderr — and why does `cmd > out.log` still show errors on screen?

_Your answer:_

## Part B — Doing it from Python

### Q6. What is `sys.argv`, and what's in `sys.argv[0]`? Given Q4, what has the shell already done to your command line before Python sees it — so what does `sys.argv` contain when you run `myscript.py *.txt "two words"`? Why is `argparse` a better habit than indexing `sys.argv` by hand?

_Your answer:_

### Q7. Compare `subprocess.run(["ls", "-l"])` with `subprocess.run("ls -l", shell=True)`: who parses the command in each case, and which is safe with untrusted input? Explain `capture_output=True`, `text=True`, `check=True`, `timeout=`, and what's in `.returncode` / `.stdout` / `.stderr`. When is `shell=True` legitimate?

_Your answer:_

### Q8. How does the shell chain commands with `&&` and `||`, and why can a deploy script without `set -e` continue past a failed step and still report success? How do you make your own Python tool a good citizen — meaningful exit codes via `sys.exit()`, errors on stderr, and `check=True` when calling children?

_Your answer:_

### Q9. How does a child process get its environment, and how do you give a child a different one (`env=`) without changing your own? Then: why does output appear instantly in a terminal but arrive late — or vanish on a crash — when piped or redirected? Explain line-buffered vs block-buffered stdout (Week 6), and the three fixes (`flush=True`, `python -u`, `PYTHONUNBUFFERED=1`).

_Your answer:_

### Q10. (Capstone — all of Phase 1.) You type `python analyze.py data.csv | grep ERROR > out.txt` and press Enter. Trace every layer: what the shell parses and expands, how `python` is resolved on PATH, the fork/exec, the pipe and redirection as file descriptors (Week 5), the read of `data.csv` (Week 6), the bytes and decoding (Week 2), the objects in RAM (Week 3), the four components doing the work (Week 1), and the exit codes travelling back. Then name one realistic way each layer can fail.

_Your answer:_
