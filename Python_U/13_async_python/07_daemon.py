import threading
import time

def monitor_te_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_te_temp, daemon=True)
t.start()

print("Main program done")