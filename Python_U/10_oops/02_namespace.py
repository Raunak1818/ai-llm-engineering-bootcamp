class Chai:
    orgin = "Indian"

print(Chai.orgin)



Chai.is_hot = True
print(Chai.is_hot)



#creating objects from class Chai


masala = Chai()
print(f"Masala {masala.orgin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False

print(f"Classes: {Chai.is_hot}")
print(f"Masala: {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)