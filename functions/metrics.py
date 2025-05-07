def calcular_metricas(tempo_seq, tempo_par, tempo_int, num_threads):
    
    speedup_par = tempo_seq / tempo_par
    speedup_int = tempo_seq / tempo_int

    eficiencia_par = speedup_par / num_threads
    eficiencia_int = speedup_int / num_threads

    print("📊 Métricas de Desempenho :")
    print(f"⚡ Tempo de execução sequencial: {tempo_seq:.5f} segundos")
    print(f"⚡ Tempo de execução paralelo  : {tempo_par:.5f} segundos")
    print(f"⚡ Tempo de execução interativo: {tempo_int:.5f} segundos")
    print("-----------------------------------------------------------------------")
    print(f"⚡ Speedup paralelo : {speedup_par:.2f}x")
    print(f"⚡ Eficiência paralelo: {eficiencia_par:.2f}")
    print("-----------------------------------------------------------------------")
    print(f"⚡ Speedup interativo: {speedup_int:.2f}x")
    print(f"⚡ Eficiência interativo: {eficiencia_int:.2f}")

