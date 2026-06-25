import threading
import time


def take_order():
    for i in range(1,4):
        print(f"taking order #{i}")
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f"brewing chai #{i}")
        time.sleep(2)



# create thread
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()


#wait for both to finish 

order_thread.join()
brew_thread.join()

print(f"All order taken and chai brewed")