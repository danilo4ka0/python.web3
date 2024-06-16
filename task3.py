from multiprocessing import Pool, cpu_count

from task2 import factorize_sync


def factorize_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def factorize_parallel(*numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize_number, numbers)


if __name__ == "__main__":
    import time

    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    results_sync = factorize_sync(*numbers)
    end_time = time.time()
    print(f"Results (sync): {results_sync}")
    print(f"Time taken (sync): {end_time - start_time} seconds")

    start_time = time.time()
    results_parallel = factorize_parallel(*numbers)
    end_time = time.time()
    print(f"Results (parallel): {results_parallel}")
    print(f"Time taken (parallel): {end_time - start_time} seconds")
