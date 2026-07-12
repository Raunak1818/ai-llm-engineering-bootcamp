import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(5)

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main Program done")