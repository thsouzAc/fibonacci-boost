from concurrent.futures import ProcessPoolExecutor
import os
import time

def fibonacci_sequencial(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_parallel(n):
    with ProcessPoolExecutor() as executor:
        futures = [
            executor.submit(fibonacci_sequencial, n - 1),
            executor.submit(fibonacci_sequencial, n - 2)
        ]
        return sum(f.result() for f in futures)
    
def calcular_metricas(tempo_seq, tempo_par, num_threads):
    if tempo_par == 0:
        print("⚠️ Tempo paralelo é zero. Não é possível calcular speedup.")
        speedup = float('inf') 
        eficiencia = float('inf')
    else:
        speedup = tempo_seq / tempo_par

        eficiencia = speedup / num_threads
    
    print("📊 Métricas de Desempenho :")
    print(f"⚡ Tempo de execução sequencial: {tempo_seq:.5f} segundos")
    print(f"⚡ Tempo de execução paralelo: {tempo_par:.5f} segundos")
    print(f"⚡ Speedup: {speedup:.2f}x")
    print(f"⚡ Eficiência: {eficiencia:.2f}x")

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