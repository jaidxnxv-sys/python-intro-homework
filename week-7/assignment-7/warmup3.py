import os 
#get and print cwd
actv_dir = os.getcwd()
print("Current working directory:", actv_dir)

#check ../data/expenses/
path = "../data/expenses.csv"
if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

#os.path.join
path = os.path.join("data", "expenses.csv")
print(path)