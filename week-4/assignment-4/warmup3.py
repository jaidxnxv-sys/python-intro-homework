#establish lists

#languages
#python, ruby, c, assembly, c++, c, java, html, swift, rust


#list 1
list_1 = ["c", "assembly", "html", "python", "java", "python"]

#list 2
list_2 = ["swift", "ruby", "rust", "java", "ruby", "assembly"]

#convert list to a set
set1 = set(list_1)
set2 = set(list_2)

#union set and print
union_set = set1.union(set2)

#convert back to list
union_list =list(union_set)
print("Full cousre list: ", union_list)

#find intersection
matches = set1 & set2
print("Matching courses: ", matches)

#languages only on list 1
print("list 1 courses:")
for lang in set1:
  print(lang)



