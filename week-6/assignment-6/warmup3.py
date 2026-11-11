def greet():
  msg = "Hello"
  #return value can be called outside function
  return msg




#error cause

#greet()
#print(msg, "Welcome to class")

#NameError: name 'msg' is not defined

msg = greet()
print(msg, "Welcome to class")

