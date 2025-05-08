from functions.fibonacci_sequencial import fibonacci_sequencial
from functions.fibonacci_parallel import fibonacci_parallel
from functions.fibonacci_interativo import fibonacci_interativo
from functions.fibonacci_interativo_parallel import fibonacci_interativo_parallel

from functions.metrics import calcular_metricas
import os
import time

# versão para varios valores de n para compensar o uso do paralelismo:

def fibonacci_interativo_batch(lista_n):
    return [fibonacci_interativo(n) for n in lista_n]


def results ( n, lista_n , num_threads ) :

    print("-----------------------------------------------------------------------")
    start = time.time()
    result_seq = fibonacci_sequencial(n)
    tempo_seq = time.time() - start
    # print(f"🔹 Fibonacci Sequencial de {n} = {result_seq}")
    # print("-----------------------------------------------------------------------")
    start = time.time()
    result_par = fibonacci_parallel(n)
    tempo_par = time.time() - start
    # print(f"🔹 Fibonacci Paralelo de {n} = {result_par}")
    # print("-----------------------------------------------------------------------")

    start = time.time()
    result_int_batch = fibonacci_interativo_batch(lista_n)
    tempo_int_batch = time.time() - start

    # print(f"🔹 Fibonacci Interativo de {n} = {result_int}")
    # print("-----------------------------------------------------------------------")
    start = time.time()
    result_int_parallel = fibonacci_interativo_parallel(lista_n)
    tempo_int_parallel = time.time() - start
    calcular_metricas(tempo_seq, tempo_par, tempo_int_batch, tempo_int_parallel, num_threads)
    print("-----------------------------------------------------------------------")