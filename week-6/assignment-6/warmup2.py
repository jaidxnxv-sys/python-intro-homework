def celsius_to_fahrenheit(celsius):
  #converts cel 2 fah
  fahrenheit = (celsius * 9/5) + 32
  #round
  return f"{celsius} Celsius is {round(fahrenheit, 1)} Fahrenheit"

print(celsius_to_fahrenheit(26))
print(celsius_to_fahrenheit(30))
print("====================")

def fahrenheit_to_celsius  (fahrenheit):
  #converts fah 2 cel
  celsius = (fahrenheit - 32) * 5/9
  #round
  return f"{fahrenheit} Fahrenheit is {round(celsius, 1)} Celsius"

print(fahrenheit_to_celsius(78.8))
print(fahrenheit_to_celsius(86))