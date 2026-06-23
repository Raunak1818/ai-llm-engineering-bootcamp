class InvalidChaiError(Exception): pass

def bill(flavor, cup):
    menu = {"Masala": 20 , "ginger": 30}
    try:
        if flavor not in menu:
            raise InvalidChaiError("flavor is not avalaible")
        if not isinstance(cup, int):
            raise TypeError("Number of Cup must be in integer")
        total = menu[flavor] * cup
        print(f"You bill for {cup} cups of {flavor} chai: {total}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thank you for coming")



bill("Mint", 3)
bill("Masala", "two")
bill("Masala", 3)