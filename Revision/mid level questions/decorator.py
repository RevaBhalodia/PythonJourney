import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.4f}s")
        return result
    return wrapper

@timer
def compute_sum(n):
    return sum(range(n))

print(compute_sum(1_000_000))