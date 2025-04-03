import time
import os
from fibonacci_sequencial import fibonacci_sequencial
from fibonacci_parallel import fibonacci_parallel
from metricas import calcular_metricas

n = 40  # valor fibonacci - altere para n maiores para ver o paralelismo funcionando de fato

num_threads = os.cpu_count() or 4  # número de threads do sistema

start = time.time()
result_seq = fibonacci_sequencial(n)
tempo_seq = time.time() - start
print(f"\n🔹 Fibonacci Sequencial({n}) = {result_seq}")

start = time.time()
result_par = fibonacci_parallel(n)
tempo_par = time.time() - start
print(f"🔹 Fibonacci Paralelo({n}) = {result_par}")

calcular_metricas(tempo_seq, tempo_par, num_threads)