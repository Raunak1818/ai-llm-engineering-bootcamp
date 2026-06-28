import threading
import time

def cpu_heavy():
    print("Crunching some numbers....")
    total = 0
    for i in range(10**8):
        total += i
    print("DONE ✅")

start = time.time()

t1 = [threading.Thread(target=cpu_heavy) for _ in range(2)] 

[t.start() for t in t1]
[t.join() for t in t1]

print(f"time taken: {time.time() - start:.2f} second")