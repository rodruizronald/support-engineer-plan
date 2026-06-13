# Phase 1 — Hardware Fundamentals Through Python (Weeks 1–8)

The detailed plan for Phase 1 of the Support Engineer learning journey.

## Goal of This Phase

Build the operator's mental model of the machine. Not the designer's, not the computer scientist's — the operator's. A SaaS or backend support engineer does not need to design CPUs, but they do need to know why a service runs out of memory, why disk I/O is slow, why a process gets killed, and what the operating system is actually doing underneath the application code. Phase 1 builds that intuition by pairing every concept with a Python experiment the learner runs on their own machine.

By the end of Phase 1, the learner should be able to answer in their own words: what physically happens when a program runs, where a variable lives, why memory and disk behave so differently, what a process is, and what role the operating system plays as the middleman between code and hardware.

## How Each Week Works

Every sub-phase (one per week) follows the same shape:

1. **Weekly Objective.** One sentence stating what this week is targeting.
2. **Brief Context.** A short paragraph framing the topic. Just enough to orient, not a tutorial.
3. **Research Questions.** A set of questions the learner answers by researching online (documentation, articles, Stack Overflow, official docs) and writes up in their own words. Answers go in that week's `solutions/answers.md`.
4. **Practical Tasks.** Several small standalone Python tasks, each focused on one concept. Each task is intentionally tiny (5–20 lines of code) so the learner can digest one idea at a time.
5. **Mini-Project.** One small but functional Python program that ties the week's tasks together into something with real meaning. Not a contrived exercise — a tool the learner could imagine actually using.

The research happens *before* the practical part each week. Theory loads the mental model; practice locks it in.

Each week lives in its own folder (e.g., `week1/`): the plan in `README.md`, and the learner's work — research answers in `solutions/answers.md` plus a Python script per task and the mini-project — in the `solutions/` subfolder.

## The 6 Sub-Phases

1. **Week 1:** [The Four Components and Their Speeds](week1/README.md).
2. **Week 2:** Binary, Bytes, and How Data Is Represented.
3. **Weeks 3–4:** Memory, Variables, and What Python Is Actually Doing.
4. **Week 5:** The Operating System as Middleman.
5. **Week 6:** Files, Paths, and I/O.
6. **Weeks 7–8:** Processes, the Shell, and Program Launch.