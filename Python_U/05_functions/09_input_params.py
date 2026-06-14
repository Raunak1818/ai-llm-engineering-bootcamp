# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing", order)

# prepare_chai(chai)
# print(chai)



chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)



def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low")       #positional

make_chai(tea= "green", sugar= "Medium", milk= "No")        #Keyword



# *args, **kwargs

def special_chai(*ingredients, **extras):
    print("Ingredient", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardmon", sweetener = "Honey", foan = "yes")


def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()
chai_order()




def chai_order(order= None):
    if order is None:
        order = []
        print(order)

chai_order()
chai_order()
