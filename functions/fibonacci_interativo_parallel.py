from functions.fibonacci_interativo import fibonacci_interativo
from concurrent.futures import ProcessPoolExecutor


def fibonacci_interativo_parallel(lista_n):
    with ProcessPoolExecutor() as executor:
        resultados = list(executor.map(fibonacci_interativo, lista_n))
    return resultados