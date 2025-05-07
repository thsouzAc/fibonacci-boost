from concurrent.futures import ProcessPoolExecutor
from functions.fibonacci_sequencial import fibonacci_sequencial

def fibonacci_parallel(n):
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(fibonacci_sequencial, n - 1),
            executor.submit(fibonacci_sequencial, n - 2)
        ]
        return sum(f.result() for f in futures)