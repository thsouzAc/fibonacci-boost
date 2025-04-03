
# calcula speedup e eficiência e tempo de execução dos códigos paralelo/sequencial
def calcular_metricas(tempo_seq, tempo_par, num_threads):
    speedup = tempo_seq / tempo_par
    eficiencia = speedup / num_threads
    print("\n Métricas de Desempenho")
    print(f"🔹 tempo de execução sequencial: {tempo_seq:.5f} segundos")
    print(f"🔹 tempo de execução paralelo: {tempo_par:.5f} segundos")
    print(f"🔹 speedup: {speedup:.2f}x")
    print(f"🔹 eficiência: {eficiencia:.2f}")
