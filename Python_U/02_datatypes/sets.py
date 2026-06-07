essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - common_spices
print(f"Only in essential: {only_in_essential}")


print(f"Is 'cloves' in essential spices?: {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices?: {'cloves' in optional_spices}")