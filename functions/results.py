from functions.fibonacci_sequencial import fibonacci_sequencial
from functions.fibonacci_parallel import fibonacci_parallel
from functions.fibonacci_interativo import fibonacci_interativo
from functions.metrics import calcular_metricas
import os
import time

def results ( n, num_threads ) :

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
    result_int = fibonacci_interativo(n)
    tempo_int = time.time() - start
    # print(f"🔹 Fibonacci Interativo de {n} = {result_int}")
    # print("-----------------------------------------------------------------------")

    calcular_metricas(tempo_seq, tempo_par, tempo_int, num_threads)
    print("-----------------------------------------------------------------------")