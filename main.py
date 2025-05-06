import time
import os
from fibonacci_sequencial import fibonacci_sequencial
from fibonacci_parallel import fibonacci_parallel
from metricas import calcular_metricas

def main():


    n = 50

    num_threads = os.cpu_count() or 4 

    start = time.time()
    result_seq = fibonacci_sequencial(n)
    tempo_seq = time.time() - start
    print("-----------------------------------------------------------------------")
    print(f"🔹 Fibonacci Sequencial de {n} = {result_seq}")
    print("-----------------------------------------------------------------------")
    start = time.time()
    result_par = fibonacci_parallel(n)
    tempo_par = time.time() - start
    print(f"🔹 Fibonacci Paralelo de {n} = {result_par}")
    print("-----------------------------------------------------------------------")
    calcular_metricas(tempo_seq, tempo_par, num_threads)
    print("-----------------------------------------------------------------------")


if __name__ == "__main__":
    main()
