import numpy as np
import numba
from numba import njit, prange

@njit(parallel=True)
# calcula Fibonacci de forma paralelizada usando OpenMP via numba
def fibonacci_parallel(n):
    if n <= 1:
        return n
    
    fib = np.zeros(n + 1, dtype=np.int64)
    fib[1] = 1

    # Loop paralelizado com OpenMP
    for i in prange(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]
