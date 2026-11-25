import csv
from fileinput import filename

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


#summary of skipped rows
rows_attempted = 0
valid_rows = []
skipped_rows = []
    
with open(filename, newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        rows_attempted += 1

        try:
            amount = float(row["amount"])
        except ValueError:
            skipped_rows.append(
                f"Row {rows_attempted}: invalid amount -> {row}"
            )
            continue

        valid_rows.append(row)
'''for row in reader:
    rows_attempted += 1

    try:
        amount = float(row["amount"])
    except ValueError:
        skipped_rows.append(
            f"Row {rows_attempted}: invalid amount -> {row}"
        )
        continue'''

    # processed valid row
print("\n--- SUMMARY ---")
print(f"Rows attempted: {rows_attempted}")
print(f"Rows parsed: {len(valid_rows)}")
print(f"Rows skipped: {len(skipped_rows)}")
print(f"Total amount: ${total_amount:.2f}")

if skipped_rows:
    print("\nSkipped rows:")
    for item in skipped_rows:
        print(f"- {item}")