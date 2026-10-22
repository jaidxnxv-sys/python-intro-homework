#age calculator
try:
  age = int(input("Enter your age: "))

  if age < 0:
    print("Invalid age")
  elif age <= 3:
    print("You are an infant.")
  elif age <= 12:
    print("You area a child.")
  elif age <= 17:
    print("You are a teenager.")
  elif age <= 64:
    print("You are a adult.")
  else:
    print("Senior")

except ValueError:
    print("Invalid Input")