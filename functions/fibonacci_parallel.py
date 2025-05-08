from concurrent.futures import ProcessPoolExecutor

def fibonacci_parallel(n, nivel=0, max_nivel=2):
    if n <= 1:
        return n
    if nivel >= max_nivel:
        return fibonacci_parallel(n - 1, nivel + 1, max_nivel) + fibonacci_parallel(n - 2, nivel + 1, max_nivel)

    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(fibonacci_parallel, n - 1, nivel + 1, max_nivel)
        f2 = executor.submit(fibonacci_parallel, n - 2, nivel + 1, max_nivel)
        return f1.result() + f2.result()
