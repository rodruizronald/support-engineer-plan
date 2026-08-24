"""Task 1 — Meet your process (practices Q3 and Q6).

Goal: use os.getpid() and os.getppid() to print your process's ID and its
parent's, then print two or three environment variables from os.environ
(like USER, HOME, PATH). Run the script twice and watch the PID change each
time — a brand-new process every run.
"""

import os 

print (" --Process Information-- ")
print ("Process ID (PID):", os.getpid())
print ("Parent Process ID (PPID):", os.getppid())

print ("\n --Environment Variables--:")
print ("- USERNAME:", os.environ.get("USERNAME"))
print ("- USERPROFILE:", os.environ.get("USERPROFILE"))
print ("- PATH:", os.environ.get("PATH"))