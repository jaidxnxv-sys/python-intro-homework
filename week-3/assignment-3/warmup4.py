#sign and parity practice
# sign refers to number line
# parity refers to even and odd
num = int(input("Enter a number: "))

#sign
if num > 0:
 print("Positive")
elif num < 0:
 print("Negative")
else:
 print("Zero")

#parity
if num % 2 == 0:
  print("Even")
else:
  print("Odd")

