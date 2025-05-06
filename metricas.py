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
