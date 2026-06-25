from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Staring {name} chai brewing....")
    time.sleep(2)
    print(f"Finishing {name} chai brewing....")

if __name__ == "__main__":
    chai_maker = [
        Process(target=brew_chai, args=(f"Chai maker #{i+1}", ))
        for i in range(4)
    ]

    # Start all process 
    for p in chai_maker:
        p.start()

    # wait for all process to finish
    for p in chai_maker:
        p.join()

    print("All chai is served")