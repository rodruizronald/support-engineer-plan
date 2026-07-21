"""Mini-project — process-probe.

A small CLI tool that does what a support engineer does when triaging a
misbehaving service: point at a process and ask the OS everything about it.
Given a PID (defaulting to this script's own process), it x-rays the process
three ways. Tasks 1, 2, 3, and 6 give you the building blocks — process
identity, the process table, file descriptors, and child processes — and
this project joins them into one diagnostic tool.

  Section 1 — Identity & environment: PID, parent PID (and the parent's
  name), the process name, the user it runs as, its status, how long it has
  been running, and its working directory.

  Section 2 — Resources it holds: memory (RSS/VMS), CPU percent, thread
  count, and number of open file descriptors — the process's footprint on
  the four components from Week 1.

  Section 3 — In the context of this machine: overall system CPU percent,
  total/available RAM, and the load average, so you can see the one process
  against the whole box.

This is the fifth artifact in your GitHub portfolio. See the Phase 1 README
(Graduation Projects) for the expected output format.
"""

# TODO: implement the mini-project.
print("process-probe — not implemented yet. Build your process/OS inspector here!")
