try:
  with open("../data/missing.txt", "r") as file:
    print(file.read())
except FileNotFoundError:
  print("File Not Found")