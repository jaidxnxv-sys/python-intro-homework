import os, csv

os.getcwd
print(os.getcwd())


#open csv

with open('../data/students.csv', 'r') as file:
  #read as dictionary
  reader = csv.DictReader(file)

  #loop
  for row in reader:
    #print name:score
    print(f"{row['name']}: {row['score']}")