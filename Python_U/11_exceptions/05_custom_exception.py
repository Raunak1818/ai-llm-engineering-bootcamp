def brew_chai(flavor):
    if flavor not in ["Masala", "ginger", "elaichi"]:
        raise ValueError("unsupported chai flavor.....")
    print(f"brewing {flavor} chai....")

brew_chai("mint")