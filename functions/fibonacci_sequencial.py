
def fibonacci_sequencial(n):
    if n <= 1:
        return n
    return fibonacci_sequencial(n - 1) + fibonacci_sequencial(n - 2)
