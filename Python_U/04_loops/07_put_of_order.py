flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavors:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")

print("Outside side of loop")