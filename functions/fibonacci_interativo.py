def fibonacci_interativo(n):
    if n <= 1 :
        return n
    k1, k2 = 0,1
    for _ in range(2, n + 1) :
        k1, k2 = k2, k1 + k2
    return k2