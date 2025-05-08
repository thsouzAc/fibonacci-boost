import time
import os

from functions.metrics import calcular_metricas
from functions.results import results


def main():
    
    n = 35
    lista_n = [3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400]
    num_threads = os.cpu_count() or 4
    results(n, lista_n ,num_threads)

if __name__ == "__main__":
    main()
