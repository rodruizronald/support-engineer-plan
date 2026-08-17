"""Task 3 — Read a big file two ways and watch memory (practices Q7).

Goal: write a file with ~200,000 numbered lines. Then count its lines twice:
once with f.read().splitlines() (whole file into RAM) and once with
for line in f: (one line at a time). Wrap each with tracemalloc.start() /
tracemalloc.get_traced_memory() and time.perf_counter(), and print the peak
memory and time for both. Same answer, wildly different footprint — expect a
difference of a few hundred times over.

Two things to look for, because both are lessons rather than bugs:

  - The streaming version may well be SLOWER in wall-clock time even though
    it uses a fraction of the memory. That trade is the point: it's what lets
    the same code survive a file bigger than your RAM.

  - The .read() version's peak memory comes out several times larger than the
    file itself, because splitlines() hands you 200,000 separate str objects,
    each carrying Week 3's object overhead.
"""

# TODO: implement this task.
print("Task 3 — not implemented yet. Compare whole-file vs streaming reads here!")
