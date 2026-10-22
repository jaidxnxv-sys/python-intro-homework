#age calculator
try:
  age = int(input("Enter your age: "))

  if age < 0:
    print("Invalid age")
  elif age <= 2:
    print("You are an infant.")
  elif age <= 12:
    print("You area a child.")
  elif age <= 19:
    print("You are a teenager.")
  elif age <= 70:
    print("You are a adult.")
  else:
    print("Age invalid")

except ValueError:
    print("Invalid Input")