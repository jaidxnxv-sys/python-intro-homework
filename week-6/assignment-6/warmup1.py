def greet(name):
  print("Hello, " + name + "!")
  print("Good Evening, " + name + "!")

greet("Jaiden")

def greet(name, greeting="How are you?"):
  print(greeting + ", " + name + "!")



greet("Jaiden")
greet("Jaiden", "What's up")
greet("Jaiden", greeting="Hello")