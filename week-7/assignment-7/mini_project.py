import csv
import os 
from datetime import datetime

file_path = "../data/expenses.csv"

#verify and open
if not os.path.exists(file_path):
  print(f"Error: {file_path} does not exist.")
  raise SystemExit

#read csv into list of dictionaries 
expenses = []

with open(file_path, newline="") as csvfile:
  reader = csv.DictReader(csvfile)

  for row in reader:
    row["amount"] = float(row["amount"])
    expenses.append(row)

#filter for food expenses 
food_expenses = [expense for expense in expenses if expense["category"] == "Food"]

#calculate total
total_food = sum(expense["amount"] for expense in food_expenses)

#todays date
today = datetime.today().strftime("%B %d, %Y")

#write report
with open("food_report.txt", "w") as report:
  report.write(f"Food Expense Report - generated {today}\n")

  for expense in food_expenses:
    report.write(f"{expense['date']}: ${expense["amount"]:.2f}\n")

  report.write(f"Total: ${total_food:.2f}\n")

#connect and print report
# mini_project.py

report = "Food Report\n"
report += "Apples: 5\n"
report += "Bananas: 3\n"

with open("food_report.txt", "w") as file:
    file.write(report)

print("food_report.txt generated successfully")