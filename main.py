import time
import os

from functions.metrics import calcular_metricas
from functions.results import results

def main():
    
    n = 35
    lista_n = [300, 320, 340, 3600, 3800, 400, 420, 440]
    num_threads = os.cpu_count() or 4
    results(n, lista_n ,num_threads)

if __name__ == "__main__":
    main()
