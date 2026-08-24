"""Task 4 — Watch a command injection happen, safely, on your own machine
(practices Q4 and Q7).

Goal: put a hostile-looking string in a variable —

    untrusted = "hello; touch INJECTED.txt"

— then pass it to a child process TWO ways, and each time print the argument
the child actually received AND check whether INJECTED.txt now exists:

  (a) as one element of a list:
      [sys.executable, "-c", "import sys; print('arg =', repr(sys.argv[1]))",
       untrusted]
      -> the child reports the WHOLE string as one literal argument,
         and no file appears.

  (b) glued into a single string with shell=True:
      -> the child reports only 'hello', and INJECTED.txt GETS CREATED.
         The shell saw the ';', cut your command in half, and ran the rest
         as a second command.

Delete the marker file when you're done.

Judge this by the FILE, not by the printed text: the word "INJECTED" appears
in both runs, because it is part of the string being echoed. The only
unambiguous proof is the side effect on disk plus the truncated argument.

On Windows, shell=True runs cmd.exe, where ';' is NOT a command separator —
use '&' in place of ';' (and `type nul > INJECTED.txt` in place of `touch`)
to see the same thing. That difference is worth noticing on its own: "which
shell am I actually handing this to?" is the question behind a lot of
cross-platform breakage.
"""

# TODO: implement this task.
print("Task 4 — not implemented yet. Show the list form vs shell=True here!")
