import time
import os

from functions.metrics import calcular_metricas
from functions.results import results

def main():
    
    n = 35
    lista_n = [300000, 320000, 340000, 360000, 380000, 400000, 420000, 440000]
    num_threads = os.cpu_count() or 4
    results(n, lista_n ,num_threads)

if __name__ == "__main__":
    main()
