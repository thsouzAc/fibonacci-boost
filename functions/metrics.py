def calcular_metricas(tempo_seq, tempo_par, tempo_int_batch, tempo_int_parallel, num_threads):
    
    speedup_par = tempo_seq / tempo_par
    speedup_int_parallel = tempo_int_batch / tempo_int_parallel

    eficiencia_par = speedup_par / num_threads
    eficiencia_int_parallel = speedup_int_parallel / num_threads

    print("📊 Métricas de Desempenho :")
    print(f"⚡ Tempo de execução sequencial: {tempo_seq:.5f} segundos")
    print(f"⚡ Tempo de execução paralelo  : {tempo_par:.5f} segundos")
    print(f"⚡ Tempo de execução interativo: {tempo_int_batch:.5f} segundos")
    print(f"⚡ Tempo de execução interativo Paralelo: {tempo_int_parallel:.5f} segundos")
    print("-----------------------------------------------------------------------")
    print(f"⚡ Speedup paralelo : {speedup_par:.2f}x")
    print(f"⚡ Eficiência paralelo: {eficiencia_par:.2f}")
    print("-----------------------------------------------------------------------")
    print(f"⚡ Speedup interativo Paralelo: {speedup_int_parallel:.2f}x")
    print(f"⚡ Eficiência interativo Paralelo: {eficiencia_int_parallel:.2f}")
