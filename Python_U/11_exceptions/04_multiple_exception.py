def process_order(item, quantity):
    try:
        price = {"Masala": 40}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry the chai is not on menu")
    except ValueError:
        print("Quantity must be in number")

process_order("Masala", 2)
process_order("ginger", 2)
process_order("Masala", "two")