class Chai:
    temperature = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.temperature)


cutting.temperature = "Mild"
cutting.cup = "Small"
print(f"After changing: {cutting.temperature}")
print(f"Cup size: {cutting.cup}")
print(f"Direct look into the class: {Chai.temperature}")


del cutting.temperature
print(f"del: {cutting.temperature}")