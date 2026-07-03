## Module 3 — Week 3: Names, Objects, and References — How Memory Actually Works

### Weekly Objective

Internalize that a Python variable is a **name bound to an object**, not a box holding a value — and see, in your own running code, how references, mutability, identity, copying, and garbage collection explain aliasing surprises ("why did my *other* variable change?"), functions that mysteriously remember state between calls, and services whose memory climbs until they get OOM-killed.

### Brief Context

Most people arrive with a "box" mental model: a variable `x` is a box, and `x = 5` puts the number 5 inside it. In Python that model is wrong, and the gap explains a whole family of confusing bugs. In Python a variable is a **name** — a label — and `x = 5` creates an integer object `5` somewhere in memory and *binds the name `x` to it*. The name and the object are two separate things: the name lives in a namespace, the object lives on the heap, and a name is just a sticky note pointing at an object. `y = x` doesn't copy anything — it puts a second sticky note on the *same* object.

That distinction is invisible until an object can **change**. Some types are **immutable** (`int`, `float`, `str`, `tuple`, `bytes`) — you can't alter them in place, so you never notice that two names share one. Others are **mutable** (`list`, `dict`, `set`) — and if two names point at the same list, changing it through one name changes what the other sees. This **aliasing** is the source of the classic "I only touched `a`, so why did `b` change too?" ticket, of the infamous mutable-default-argument bug, and of copies that don't actually copy.

The other half of the week is *when objects die*. An object lives on the heap; CPython frees it the moment nothing references it anymore (**reference counting**), with a backup **cycle collector** for objects that reference each other. Crucially, in a garbage-collected language you don't leak by *forgetting to free* — you leak by *never letting go*: a cache that never evicts, a global list you keep appending to, a handler that keeps every request it's ever seen. The object can't be collected because something still points at it. That's the "the service runs fine for two days, then falls over" ticket — a slow memory climb that ends in the OOM killer.

This week you build x-ray vision for names and objects. First the model — names vs objects, references, identity, mutability, and garbage collection. Then the Python specifics — `is` vs `==`, `id()`, shallow vs deep copy, the mutable-default trap, and watching reference counts rise and fall. It ties directly back to Weeks 1 and 2: an object has a **byte size** (Week 2), it lives in **RAM** and may cross the slow boundaries to disk or the network (Week 1), and it survives only as long as **something references it** (this week). Those three facts together explain nearly every "why is this slow / why is memory growing" question you'll ever get.

> **How to work through the week:** Answer the research questions in your own words first (write them in `solutions/answers.md`), then do the practical tasks (one script each, in `solutions/`). When you're ready, build this week's **graduation project** — see [Phase 1 → Graduation Projects](../README.md#graduation-projects). Theory loads the mental model; the code locks it in.

### Research Questions

Answer each in your own words in `solutions/answers.md`. Don't copy-paste definitions — explain them as if to a friend.

#### Part A — Names, objects, and references

1. The "box" model says a variable is a box and `x = 5` puts a value in it. In Python that's wrong. What does `x = 5` *actually* do — and what's the difference between the **name** `x` and the **object** `5`? Where does each of the two live?
2. What happens when you write `b = a`? When does that give you "a second name for the same object" versus "a copy"? Explain **aliasing**, and say why you can *observe* it with a list but not with an integer.
3. What's the difference between **identity** (`is`) and **equality** (`==`)? What does `id()` give you? Why is `a is b` sometimes surprisingly `True` for small integers or short strings (interning) — and why should you never use `is` to compare two *values*?
4. Which common types are **mutable** and which are **immutable** (`int`, `float`, `str`, `tuple`, `bytes` vs `list`, `dict`, `set`)? What does "immutable" actually forbid — and does it stop you from *rebinding the name* to a different object?
5. How does Python decide an object can be thrown away (**reference counting** plus a **cycle collector**)? If you can't forget to free memory in Python, how do you still get a **memory leak** — i.e., how do you leak by *keeping references*? Give a concrete example (an unbounded cache, a global list that only ever grows, a buffer you keep appending to).

#### Part B — How Python shows you this

6. **Shallow vs deep copy.** You copy a list of lists with `x[:]` or `list(x)`, then change something *inside* one of the nested lists — why does the change show up in the "copy" too? When do you actually need `copy.deepcopy`, and what does it cost you?
7. **The mutable default argument trap.** Why does `def add(item, bucket=[])` keep accumulating items across separate calls? Explain *when* that default list is created (hint: once, at definition time — not per call), and the correct `bucket=None` fix. Why is this a bug support engineers really do see?
8. Is Python "pass by value" or "pass by reference"? Explain the real answer — "pass by object reference" (a.k.a. pass by assignment) — by contrasting two cases inside a function: **reassigning** a parameter (`x = x + 1`) versus **mutating** it (`x.append(1)`). Which one does the caller see, and why?
9. How would you *measure* what you've learned? Explain `sys.getsizeof()` and `sys.getrefcount()`. Why does a plain Python `int` take roughly 28 bytes when the same value in C fits in 4 (tie this back to Week 2's byte sizes — where does the extra go)? And why is the refcount you print always one higher than you expected?
10. *(Tie-back to Weeks 1–2.)* Put the three weeks together. An object has a byte size (Week 2); it lives in RAM and may be written to disk or sent over the network (Week 1); and it stays alive only as long as something references it (this week). Using all three, explain step by step how a service's memory can climb until it's OOM-killed — and, given that model, where you'd look *first* to find the leak.

### Practical Tasks

Each task is a separate, tiny Python file (think 5–20 lines). Run each one, look at the output, and write one sentence in your notes about what it showed you. Each task practices something from the questions above. **Task 6 is optional** — a stretch for when you want to go further.

1. **Task 1 — Two names, one object.** *(Practices Q1 and Q2.)* Write `a = [1, 2, 3]`, then `b = a`, then `b.append(4)` — and print both `a` and `b` to see they changed *together*. Print `id(a)` and `id(b)` to prove they're the same object. Then repeat the whole thing with an integer (`a = 5; b = a; b = b + 1`) and show that this time `a` is untouched. **Concepts:** assignment as binding, `id()`, `.append()`, aliasing.
2. **Task 2 — `is` vs `==`.** *(Practices Q3.)* Make two lists with identical contents and show that `==` is `True` but `is` is `False`. Then show integer interning: `a = 256; b = 256; print(a is b)` (usually `True`) versus `a = 257; b = 257; print(a is b)` (often `False`). Let this convince you to compare values with `==` and reserve `is` for `None`. **Concepts:** `is`, `==`, `id()`, small-int interning.
3. **Task 3 — Mutate vs rebind.** *(Practices Q4.)* Try `s = "cat"; s[0] = "b"` and catch the `TypeError` — strings are immutable. Then show that `s = s + "!"` gives you a *new* object (print `id(s)` before and after — it changes), while `lst = [1, 2]; lst.append(3)` keeps the *same* object (its `id` stays put). See the difference between changing a name and changing an object. **Concepts:** immutability, `TypeError`, rebinding vs mutating, `id()`.
4. **Task 4 — The mutable default argument trap.** *(Practices Q7.)* Write the buggy `def add(item, bucket=[]): bucket.append(item); return bucket`, call it three times with different items, and watch the same list grow across calls (print `id(bucket)` to prove it's literally the same list each time). Then write the `bucket=None` fix and show each call now starts fresh. **Concepts:** default arguments, definition-time evaluation, the `None` idiom.
5. **Task 5 — Shallow copy vs deep copy.** *(Practices Q6.)* Take a nested list like `original = [[1, 2], [3, 4]]`, make a shallow copy (`copy.copy(original)` or `original[:]`), then run `original[0].append(99)` and watch the change bleed into the "copy." Now do the same with `copy.deepcopy(original)` and show it stays isolated. **Concepts:** `copy.copy`, `copy.deepcopy`, nested mutation, slicing.
6. **Task 6 — Watch references rise and fall.** *(Optional — practices Q5 and Q9.)* Create an object, print `sys.getrefcount(obj)`, then add it to a list and print the count again (it goes up); `del` the list and watch it drop. As a bonus, use `weakref.finalize(obj, print, "collected!")` to see the *exact* moment the object is freed when the last reference goes away, and print `sys.getsizeof()` of a small int, a huge int, and a list to tie the object header back to Week 2's byte sizes. **Concepts:** `sys.getrefcount`, `del`, `weakref.finalize`, `sys.getsizeof`.
