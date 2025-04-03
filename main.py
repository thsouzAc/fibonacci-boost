import time
import os
from fibonacci_sequencial import fibonacci_seq
from fibonacci_parallel import fibonacci_parallel


n = 120  
num_threads = os.cpu_count() or 4 


start = time.time()
result_seq = fibonacci_seq(n)
tempo_seq = time.time() - start
print(f"\n🔹 Fibonacci Sequencial({n}) = {result_seq}")


start = time.time()
result_par = fibonacci_parallel(n)
tempo_par = time.time() - start
print(f"🔹 Fibonacci Paralelo({n}) = {result_par}")
