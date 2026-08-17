# Week 6 — Answers: Files, Paths, and I/O

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — Files, paths, and the filesystem

### Q1. What is a file underneath ("a named sequence of bytes plus metadata")? What does the filesystem add on top of the raw disk from Week 1? What is a directory really, and why is a file extension a hint rather than a fact?

_Your answer:_

### Q2. Absolute vs relative paths, and the current working directory: what's the difference? Why can a script that opens `config.yaml` work from your editor and fail under cron or in a container? What do `.`, `..`, `~`, and `/` vs `\` mean?

_Your answer:_

### Q3. Metadata vs contents: what does the OS track about each file (size, modification time, owner, permission bits) — the `ls -l` fields? Explain read/write/execute for user/group/other, what "Permission denied" is telling you, and why renaming a huge file is instant while copying it is slow.

_Your answer:_

### Q4. Buffering and the OS page cache: what are they and why do they exist (tie back to Week 1's latency hierarchy)? What's the difference between `flush()` and `fsync()`, what happens to buffered data when a process is `SIGKILL`ed (Week 5), and how can a reader catch a file half-written?

_Your answer:_

### Q5. What happens to a running service when the disk fills up (`ENOSPC`)? Why does deleting a big log file sometimes not free the space until the process restarts (tie back to Week 5's file descriptors), and what is log rotation for?

_Your answer:_

## Part B — How Python does file I/O

### Q6. Text mode vs binary mode in `open()`: what do the mode characters (`r`, `w`, `a`, `x`, `+`, `b`) do, and what exactly does `w` do to an existing file? Which mode gives `str` and which gives `bytes`, what does text mode silently do for you (Week 2 encodings, the `encoding=` argument), and when must you use binary?

_Your answer:_

### Q7. Why can `.read()` on a 4 GB file take down a service that handles it fine line-by-line? Compare `f.read()`, `for line in f:`, and `f.read(chunk_size)` by memory footprint — and using Weeks 1 and 3, explain why streaming is the default habit you want.

_Your answer:_

### Q8. Why prefer `pathlib` over gluing strings together? What does `Path` give you (`/`, `.name`, `.suffix`, `.parent`, `.exists()`, `.stat()`, `.resolve()`), and why does `Path(__file__).parent / "data.txt"` fix the "my script can't find its own data file" bug from Q2?

_Your answer:_

### Q9. What do `FileNotFoundError`, `PermissionError`, and `IsADirectoryError` each tell you about where to look? Why is wrapping `open()` in `try`/`except` preferred over checking `path.exists()` first, and what can change in the gap between the check and the open? Then explain the atomic write pattern (temp file + `os.replace()`) and what it protects a reader from.

_Your answer:_

### Q10. (Tie-back to Weeks 1, 2, 3, and 5.) Trace `text = open("data.txt").read()` all the way down: the path resolved against the working directory, the system call and file descriptor (Week 5), the disk read and why it's the slow part (Week 1), the bytes and the decode (Week 2), and the `str` object now in RAM with a name bound to it (Week 3). Then name one realistic way each layer can fail.

_Your answer:_
