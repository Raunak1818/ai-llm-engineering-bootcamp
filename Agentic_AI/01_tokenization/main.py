import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

txt = "Hey there! My name is Raunak Jaiswal"

token = enc.encode(txt)

print(f"token = {token}")
# token = [25216, 1354, 0, 3673, 1308, 382, 13412, 140276, 643, 1873, 22314]

decoded = enc.decode([25216, 1354, 0, 3673, 1308, 382, 13412, 140276, 643, 1873, 22314])
print(f"Decoded = {decoded}")