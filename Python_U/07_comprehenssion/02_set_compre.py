favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai", "Lemaon tea", "Green Tea", "Elaichi Chai"
]

# {expression for item in items if condition}   = formula 

unique_chai = {chai for chai in favourite_chais if len(chai) > 8 }

print(unique_chai)



recipes = {
    "Masala Chai": ["ginger", "cardamon", "clove"],
    "Elaichi Chai": ["cardamon", "milk"],
    "spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)