names = ["Alice", "Bob", "Chalie", "David", "Eve"]
cutomer_name = input("Enter a name: ")
output = [name for name in names if name.lower().find(cutomer_name.lower()) != -1]
print("Matching names:", output)