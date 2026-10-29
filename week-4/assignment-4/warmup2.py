#dictionary of student enrollment

student_info = {
    "name": "Alice",
    "grade": "A",
    "subjects": ["Mathematics"]
}

#unpack tuples into their key and value

for key in student_info.items():
  print(key, student_info)

#add a new key and update list

student_info["graduated"] = False

print(student_info)


