import csv

valid_rows = []

try:
  with open("../data/messy_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
      try:
        name = row["name"]
        category = row["category"]
        amount = float(row["amount"])

        valid_rows.append({
            "name": name,
            "category": category,
            "amount": amount
        })

      except ValueError:
        print(f"Skip invalid amount: {row}")
      except KeyError:
        print(f"Skip missing colomn: {row}")

except FileNotFoundError:
  print("Error: ../data/messy_data.csv not found.")
  exit()

print("\nSummary")
print("-------")
print(f"Valid rows: {len(valid_rows)}")

total_amount = sum(row["amount"] for row in valid_rows)
print(f"Total amount: {total_amount:.2f}")

print("\nClean data:")
for row in valid_rows:
  print(row)


