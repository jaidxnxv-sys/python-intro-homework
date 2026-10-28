#school stats
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
#top scorer
#score variables 
top_score = 0
top_student = 0 
#loop list 
for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_student = student["name"]

#output results
print("Top scorer:", top_student, top_score)

#school stats
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

#score variables 
top_score = 0
top_student = 0 
#loop list 
for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_student = student["name"]

#output results
print("Top scorer:", top_student, top_score)


#student average
total_score = 0
for student in students:
    total_score += student["score"]
average_score = total_score / len(students)
print("Class Average:", average_score)

#subjects
subject_list = set()
for student in students:
    subject_list.add(student["subject"])
print("Subjects offered:", subject_list)

#high scorers
high_scorers = []
for student in students:
    if student["score"] >= 75:
        high_scorers.append(student["name"])
print("High Scorers:", high_scorers)




