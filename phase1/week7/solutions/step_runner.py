"""Mini-project — step-runner.

A small CLI tool that does what every deploy script, CI job, and release
checklist does: run a list of commands in order, and report honestly on what
happened. Tasks 2, 3, 4, and 5 give you the building blocks — PATH
resolution, capturing a child's output and exit code, the safe list form, and
keeping stdout and stderr apart — and this project joins them into one
runner.

  Section 1 — The plan: for each step, resolve the program on PATH with
  shutil.which() and print where it will actually come from, BEFORE running
  anything. A step whose program can't be found is reported now, not
  halfway through.

  Section 2 — Execution: run each step with subprocess.run() using the list
  form (never shell=True), capturing stdout and stderr separately and timing
  each one. Print a live line per step with its exit code and duration, and
  echo the stderr of anything that fails. Stop at the first failure unless
  --keep-going is passed.

  Section 3 — Summary: a table of step / status / exit code / duration, the
  totals, and the runner's own exit code — 0 only if every step passed.

This is the sixth and final artifact in your GitHub portfolio, and the
capstone of Phase 1. See the Phase 1 README (Graduation Projects) for the
expected output format.
"""

# TODO: implement the mini-project.
print("step-runner — not implemented yet. Build your command step runner here!")
