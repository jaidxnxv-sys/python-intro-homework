#linear searching

names = ["Jay", "Cathy", "Marcus", "Roweena", "Becky", "Sarah"]

name_search = input("Search Name: ")
found = False

for i in range(len(names)):
  if names[i] == name_search:
    print(f"Found {name_search} at index {i}.")
    found = True
    break

if not found:
  print(f"{name_search} was not found in list.")