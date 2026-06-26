import threading
import time

def boil_milk():
    print(f"Boiling milk....")
    time.sleep(2)
    print("Milk Boiled")


def toast_bun():
    print("toasting bun....")
    time.sleep(3)
    print("Done with toasted bun")

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

start = time.time()

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Breakfast is ready {end - start:.2f}")