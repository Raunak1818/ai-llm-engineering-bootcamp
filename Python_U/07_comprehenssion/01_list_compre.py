menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]
# [expression for item in items if condition]    = formula 

# iced_tea = [tea for tea in menu if "Iced" in tea]
iced_tea = [tea for tea in menu if len(tea) > 10]
iced_tea = [tea for tea in menu if len(tea) < 10]


print(iced_tea)