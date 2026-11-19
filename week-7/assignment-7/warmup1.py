#file reader
#try:
# with open('notes.txt', 'r') as file:
#  for line in file:
#    print(line.strip())
#except FileNotFoundError:
#  print("The file 'notes.txt' was not found.")

with open("../data/notes.txt", "r") as file:
    for number, line in enumerate(file, start=1):  # start=1 for 1-based numbering
        stripped_line = line.strip()  # remove trailing newline
        print(f"Line {number}: {stripped_line}")
