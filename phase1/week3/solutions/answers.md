# Week 3 — Answers: Names, Objects, and References

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — Names, objects, and references

### Q1. The "box" model is wrong in Python. What does `x = 5` actually do? What's the difference between the name `x` and the object `5`, and where does each one live?

_Your answer:_

### Q2. What happens with `b = a`? When is that a second name for the same object vs a copy? Explain aliasing, and why you can observe it with a list but not with an integer.

_Your answer:_

### Q3. Identity (`is`) vs equality (`==`): what does each check, and what does `id()` return? Why is `a is b` sometimes surprisingly `True` for small ints/short strings (interning), and why should you never use `is` to compare values?

_Your answer:_

### Q4. Which common types are mutable vs immutable (int, float, str, tuple, bytes vs list, dict, set)? What does "immutable" forbid — and does it stop you from rebinding the name to a different object?

_Your answer:_

### Q5. How does Python decide an object can be freed (reference counting + cycle collector)? If you can't forget to free memory, how do you still get a memory leak by keeping references? Give a concrete example.

_Your answer:_

## Part B — How Python shows you this

### Q6. Shallow vs deep copy: you copy a list of lists, then change something nested — why does it show up in the "copy"? When do you need `copy.deepcopy`, and what does it cost?

_Your answer:_

### Q7. The mutable default argument trap: why does `def add(item, bucket=[])` accumulate across calls? When is the default created, and what's the correct `bucket=None` fix?

_Your answer:_

### Q8. Is Python "pass by value" or "pass by reference"? Explain "pass by object reference" by contrasting reassigning a parameter (`x = x + 1`) vs mutating it (`x.append(1)`) inside a function. Which does the caller see, and why?

_Your answer:_

### Q9. `sys.getsizeof()` and `sys.getrefcount()`: why does a plain Python `int` take ~28 bytes when C fits it in 4 (tie back to Week 2 — where does the extra go)? Why is the refcount you print always one higher than expected?

_Your answer:_

### Q10. (Tie-back to Weeks 1–2.) An object has a byte size (Week 2), lives in RAM and may hit disk/network (Week 1), and stays alive only while referenced (this week). Using all three, explain how a service's memory climbs until it's OOM-killed — and where you'd look first for the leak.

_Your answer:_
