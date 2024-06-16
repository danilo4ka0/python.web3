import multiprocessing
from time import time

def factorize_sync(*numbers):
    result = []
    for number in numbers:
        result.append([i for i in range(1, number + 1) if number % i == 0])
    return result

def factorize(number):
    return [i for i in range(1, number + 1) if number % i == 0]

def factorize_async(*numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(factorize, numbers)
    return result

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]

    start = time()
    result_sync = factorize_sync(*numbers)
    end = time()
    print(f"Synchronous version took {end - start:.2f} seconds")

    start = time()
    result_async = factorize_async(*numbers)
    end = time()
    print(f"Asynchronous version took {end - start:.2f} seconds")

    # Validation
    assert result_sync == result_async, "The results do not match"

    a, b, c, d = result_async

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
