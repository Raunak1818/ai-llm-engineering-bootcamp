class A:
    label = "A: Base Class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    pass

cup = D()
print(cup.label)
print(D.__mro__)