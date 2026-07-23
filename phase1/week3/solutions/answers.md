# Week 3 — Answers: Names, Objects, and References

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — Names, objects, and references

### Q1. The "box" model is wrong in Python. What does `x = 5` actually do? What's the difference between the name `x` and the object `5`, and where does each one live?

_Your answer:When we write x = 5, Python does not store the number 5 inside the variable x. Instead, it creates (or reuses) an object with the value 5 and makes the name x point to that object._
_The object contains the actual data and lives in RAM. The name x is not the data itself; it is simply a reference that Python uses to find the object._
_That is why variables in Python are not boxes that hold data, but names that refer to objects._

### Q2. What happens with `b = a`? When is that a second name for the same object vs a copy? Explain aliasing, and why you can observe it with a list but not with an integer.

_Your answer: When we write b = a, Python does not create a copy. Both names point to the same object, which is called aliasing. If the object is mutable, like a list, changes are visible through both names. If it is immutable, like an integer, a new object is created, so the other name is not affected._

### Q3. Identity (`is`) vs equality (`==`): what does each check, and what does `id()` return? Why is `a is b` sometimes surprisingly `True` for small ints/short strings (interning), and why should you never use `is` to compare values?

_Your answer:The == operator checks whether two objects have the same value. The is operator checks whether two names refer to the same object in memory. The id() function returns the object's unique identifier. Python reuses some small integers and short strings, so is may return True. However, values should always be compared with == because is only checks object identity._

### Q4. Which common types are mutable vs immutable (int, float, str, tuple, bytes vs list, dict, set)? What does "immutable" forbid — and does it stop you from rebinding the name to a different object?

_Your answer: The most common immutable types in Python are int, float, str, tuple, bytes, and bool. The most common mutable types are list, dict, and set._

_An object is immutable if its contents cannot be changed after it has been created. For example, a string cannot have one of its characters modified directly._

_However, this does not mean that the variable cannot change. A variable name can stop pointing to one object and start pointing to a different one. For example, when you write x = 5 and later x = 6, Python does not modify the object 5. Instead, x simply points to the object 6._

### Q5. How does Python decide an object can be freed (reference counting + cycle collector)? If you can't forget to free memory, how do you still get a memory leak by keeping references? Give a concrete example.

_Your answer:Python uses reference counting and a garbage collector to free objects that are no longer referenced. However, a memory leak can still happen if a program keeps references to objects it no longer needs. For example, if a list stores every user request and never removes old data, memory usage will continue to grow._

## Part B — How Python shows you this

### Q6. Shallow vs deep copy: you copy a list of lists, then change something nested — why does it show up in the "copy"? When do you need `copy.deepcopy`, and what does it cost?

_Your answer: A shallow copy creates a new outer structure, but the nested objects are still shared. A nested list is simply a list stored inside another list, such as [1, 2] inside [[1, 2], [3, 4]]. Because both copies share the same nested list, changing that list also changes what both copies display._

_A deep copy creates new copies of all nested objects (an object is any value stored in memory, such as a number, string, list, or dictionary), making the two structures completely independent._

_You should use copy.deepcopy() when you need to modify a nested structure without affecting the original. However, it uses more memory and takes more time because Python must visit and copy every object in the entire structure.._

### Q7. The mutable default argument trap: why does `def add(item, bucket=[])` accumulate across calls? When is the default created, and what's the correct `bucket=None` fix?

_Your answer:A default argument is created only once, when Python defines the function. If the default is a list, the same list is reused every time the function is called, so values keep accumulating. The correct solution is to use bucket=None and create a new list inside the function when needed._

### Q8. Is Python "pass by value" or "pass by reference"? Explain "pass by object reference" by contrasting reassigning a parameter (`x = x + 1`) vs mutating it (`x.append(1)`) inside a function. Which does the caller see, and why?

_Your answer:Python uses pass by object reference. The function receives a reference to the same object. If the function modifies a mutable object, like a list, the caller sees the change. If the parameter is reassigned to a new object, only the local variable changes, so the caller is not affected._

### Q9. `sys.getsizeof()` and `sys.getrefcount()`: why does a plain Python `int` take ~28 bytes when C fits it in 4 (tie back to Week 2 — where does the extra go)? Why is the refcount you print always one higher than expected?

_Your answer:A Python integer uses more memory because it is a complete object. Besides storing its numeric value, it also stores information such as its type, its reference count, and other internal data that Python needs to manage the object. In C, an integer usually stores only the numeric value._

_sys.getrefcount() usually reports one extra reference because Python temporarily creates another reference when the object is passed as an argument to the function. That temporary reference exists only while the function is running._

### Q10. (Tie-back to Weeks 1–2.) An object has a byte size (Week 2), lives in RAM and may hit disk/network (Week 1), and stays alive only while referenced (this week). Using all three, explain how a service's memory climbs until it's OOM-killed — and where you'd look first for the leak.

_Your answer: (OOM stands for Out Of Memory. It happens when a program tries to use more RAM than is available or allowed)._

_A service can run out of memory if it keeps creating objects and keeps references to them even after they are no longer needed. As long as a reference exists, Python considers the object to still be in use and cannot free its memory. If this continues, RAM usage keeps increasing until the program becomes slow or the operating system terminates it because it has run out of memory._

_To investigate a memory leak, I would first check lists, dictionaries, sets, caches, queues, and global variables that keep growing without removing old data. These structures often keep references to objects longer than necessary, preventing Python from releasing their memory.._
