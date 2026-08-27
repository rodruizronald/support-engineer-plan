"""Task 3 — Run a child and capture what it says (practices Q7).

Goal: use subprocess.run([...], capture_output=True, text=True) to run a
command that succeeds, and print .returncode, .stdout, and .stderr separately
so you can see the two streams stay apart. Then run a command that FAILS,
print its non-zero .returncode, and finally run it again with check=True
inside a try/except subprocess.CalledProcessError to watch Python turn a bad
exit code into an exception.
"""


import subprocess
import sys


print("--- SUCCESSFUL CHILD PROCESS ----")

#ejecutamos otro Python como child process.
successful_result = subprocess.run(
    [
        sys.executable,
        "-c",
        'import sys; print("Hello from stdout"); print("Hello from stderr", file=sys.stderr)'
    ],
    capture_output=True,
    text=True
)

print("Return code:", successful_result.returncode)
print("STDOUT:")
print(successful_result.stdout)

print("STDERR:")
print(successful_result.stderr)


print("--- FAILED CHILD PROCESS ---")

# ejecutamos otro Python que termina intencionalmente con exit code 3.
failed_result = subprocess.run(
    [
        sys.executable,
        "-c",
        'import sys; print("Something went wrong", file=sys.stderr); sys.exit(3)'
    ],
    capture_output=True,
    text=True
)

print("Return code:", failed_result.returncode)
print("STDOUT:")
print(failed_result.stdout)

print("STDERR:")
print(failed_result.stderr)


print("--- FAILED CHILD WITH check=True ---")

try:
    subprocess.run(
        [
            sys.executable,
            "-c",
            'import sys; print("Something went wrong", file=sys.stderr); sys.exit(3)'
        ],
        capture_output=True,
        text=True,
        check=True
    )

except subprocess.CalledProcessError as error:
    print("Caught CalledProcessError")
    print("Return code:", error.returncode)
    print("STDOUT:")
    print(error.stdout)

    print("STDERR:")
    print(error.stderr)