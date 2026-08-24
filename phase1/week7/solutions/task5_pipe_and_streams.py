"""Task 5 — Build a pipe, and split the streams (practices Q5).

Goal: two parts.

  (a) Recreate `cmd1 | cmd2` in Python: start a first child with
  subprocess.Popen([...], stdout=subprocess.PIPE), pass its .stdout as the
  second child's stdin=, and read the final result. Use short `python -c`
  commands on both ends so it behaves the same on every OS.

  (b) Write one line to sys.stdout and one to sys.stderr from this script,
  then run it redirecting only stdout:

      python task5_pipe_and_streams.py > out.txt

  and watch the error line stay on your screen while the normal line lands in
  the file.
"""

# TODO: implement this task.
print("Task 5 — not implemented yet. Wire two processes together, then split the streams!")
