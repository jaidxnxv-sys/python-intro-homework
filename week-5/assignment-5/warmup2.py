# while loop input val

while True:
  user_input = input("Enter positive digit: ")

  try:
    num = int(user_input)

    if num > 0:
      print(f"Nice: {num}")
      break

    else:
      print("Try a positive digit.")
  except ValueError:
    print("Try a positive digit.")