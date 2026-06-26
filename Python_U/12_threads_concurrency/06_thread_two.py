import threading
import time

def prepare_chai(_type, waittime):
    print(f"{_type} chai preparing.....")
    time.sleep(waittime)
    print(f"{_type} chai prepared")


t1 = threading.Thread(target= prepare_chai, args=("masala", 2))
t2 = threading.Thread(target= prepare_chai, args=("ginger", 3))

t1.start()
t2.start()
t1.join()
t2.join()