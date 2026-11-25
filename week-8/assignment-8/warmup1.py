while True:
  try:
    number = float(input("Enter a Number: "))
    print("You entered: ", number)
    break
  except ValueError:
    print("Invalid. Try Again.")




