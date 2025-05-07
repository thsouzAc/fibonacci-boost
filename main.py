import time
import os

from functions.metrics import calcular_metricas
from functions.results import results


def main():
    
    n = 7
    num_threads = os.cpu_count() or 4 
    results(n, num_threads)

if __name__ == "__main__":
    main()
