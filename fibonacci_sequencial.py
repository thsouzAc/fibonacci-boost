# função para comparar os resultados sequencial/paralelo > 

def fibonacci_seq(n) :
    if n <= 1 :
        return n
    n1, n2 = 0, 1
    for _ in range(2, n + 1 ) :
        n1, n2 = n2, n1 + n2

    return n2