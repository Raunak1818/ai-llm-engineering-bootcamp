device_status = input("Enter the device status: ").lower()
temperature = int(input("Enter the temperature: "))

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
elif device_status == "offline":
    print("Device is offline")
else:
    print("unknown device status")