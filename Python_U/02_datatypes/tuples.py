masala_spices = ("cardamon", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main Masala spice: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamon_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cardamon_ratio}")
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cardamon_ratio}")


# Membership testing

print(f"Is ginger in masala spices? {'cinnamon' in masala_spices}")