def chai_flavor(flavor = "Masala"):
    """Return the flavor of chai"""
    chai = "ginger"
    return flavor


print(chai_flavor.__doc__)
print(chai_flavor.__name__)



def generate_bill(chai = 0, samosa = 0):
    """
    Calculate the total bill chai and samosa

    :param chai: Number of chai cup (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message)

    """
    total = chai * 10 + samosa *15
    return total, "thanku for visiting chaicode.com"

print(generate_bill())