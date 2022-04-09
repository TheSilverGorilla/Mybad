import time

def time_checker(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        print(f"Finished in {end-start} seconds")
    return wrapper()
