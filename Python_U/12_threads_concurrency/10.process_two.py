from multiprocessing import Process
import time

def cpu_heavy():
    print("Crunching the number...")
    total = 0
    for i in range(10**9):
        total += i
    print("DONE ✅")


p1 = [Process(target=cpu_heavy) for _ in range(2)]

if __name__ == "__main__":

    start = time.time()

    [p.start() for p in p1]
    [p.join() for p in p1]

    print(f"Time taken: {time.time() - start:.2f} second")