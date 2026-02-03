import time
import threading

# Total number of loop iterations
N = 100_000_000


def count(n):
    """
    Counts from 0 to n - 1.
    This is a CPU-bound operation (pure computation, no I/O).
    """
    for _ in range(n):
        pass


# ============================================================
# 1) NO THREADS
# ============================================================

# time.perf_counter() starts a high-resolution stopwatch.
# It measures real elapsed wall-clock time, not CPU time.
start = time.perf_counter()

# Run the counting function directly on the main thread.
# The CPU executes this loop continuously.
count(N)

# Stop the stopwatch and calculate how much real time passed.
elapsed = time.perf_counter() - start

# Print total wall-clock time seen by the timer.
print("No thread:", elapsed)


# ============================================================
# 2) SINGLE THREAD
# ============================================================

# Start a new stopwatch.
# perf_counter() does NOT care which thread runs the code,
# it only measures total real time that passes.
start = time.perf_counter()

# Create a thread that will run the same count() function.
t = threading.Thread(target=count, args=(N,))

# Start the thread.
# The OS schedules this thread, but Python's GIL ensures
# only one thread executes Python bytecode at a time.
t.start()

# Join blocks the main thread until the worker thread finishes.
t.join()

# Stop stopwatch after the thread completes.
elapsed = time.perf_counter() - start

print("Single thread:", elapsed)


# ============================================================
# 3) MULTIPLE THREADS
# ============================================================

threads = []

# Start stopwatch again.
# perf_counter() counts total wall time across ALL threads.
start = time.perf_counter()

# Create 4 threads and split the work evenly.
for _ in range(4):
    # Each thread counts 1/4 of N
    t = threading.Thread(target=count, args=(N // 4,))
    threads.append(t)

    # Start thread execution.
    # Threads interleave execution due to the GIL,
    # rather than running in parallel on multiple cores.
    t.start()

# Wait for ALL threads to finish.
for t in threads:
    t.join()

# Stop stopwatch after all threads complete.
elapsed = time.perf_counter() - start

print("4 threads:", elapsed)
