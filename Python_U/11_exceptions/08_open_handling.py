# file = open("order.txt", "w")

# try:
#     file.write("Masala chai - 2 cup")
# finally:
#     file.close()



with open("order.txt", "w") as file:
    file.write("Ginger tea - 5 cups")