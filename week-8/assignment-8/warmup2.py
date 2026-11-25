first_number = float(input("Numerator: "))
second_number = float(input("Denominator: "))

try:
  result = first_number / second_number
  print("result:", round(result, 2))
except ZeroDivisionError:
  print("Cant divide zero.")

