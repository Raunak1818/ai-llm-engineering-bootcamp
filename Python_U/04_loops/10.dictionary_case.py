users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 180, "coupon": "G50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "G50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"User id: {user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")