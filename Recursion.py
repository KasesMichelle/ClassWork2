# Print numbers 1 to 9
for i in range(1, 10):
    print(i)

# Recursive Fibonacci (inefficient)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 20):  # Reduced from 50 to 20 to avoid slowness
    print(i, ":", fibonacci(i))

# Optimized Fibonacci using memoization (manual cache)
cache = {}

def fib2(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        value = 1
    else:
        value = fib2(n - 1) + fib2(n - 2)
    cache[n] = value
    return value

for i in range(1, 50):
    print(f"{i} Term: {fib2(i)}")

# Optimized Fibonacci using built-in caching
from functools import lru_cache

@lru_cache(maxsize=1000)
def fib3(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2)

for i in range(1, 2000):
    print(f"fib3({i}) = {fib3(i)}")


    def tower_of_hanoi(n, source, destination_rod, auxiliary_rod):
        if n == 1:
            print("move disk 1 from source ", source, " to destination ", destination_rod)
            return
        tower_of_hanoi(n - 1, source, auxiliary_rod, destination_rod)
        print("Move disk ", n, "from source ", "to destination ", destination_rod)
        tower_of_hanoi(n - 1, auxiliary_rod, destination_rod, source)


    n = 3
    tower_of_hanoi(n, "A", "B", "C")
