def factorize_sync(*numbers):
    def factorize_number(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    return [factorize_number(n) for n in numbers]


if __name__ == "__main__":
    import time

    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    results = factorize_sync(*numbers)
    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken (sync): {end_time - start_time} seconds")
