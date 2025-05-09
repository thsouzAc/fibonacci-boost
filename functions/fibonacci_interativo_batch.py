from functions.fibonacci_interativo import fibonacci_interativo

def fibonacci_interativo_batch(lista_n):
    return [fibonacci_interativo(n) for n in lista_n]