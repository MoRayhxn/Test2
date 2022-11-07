# students = ["Hermione", "Harry", "Ron"]
## how to print them all out one by one neatly
# for student in students:
#     print(student)


## this code will show the students in order with a label so 0, 1 ,2. to make it start at 1 visually we can do i + 1, in the print function
# for i in range (len(students)):
#     print(i + 1, students[i])

# houses = ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slyhterin")

# students = {
#     "Hermione": houses[0], 
#     "Harry": houses[0],
#     "Ron": houses[0],
#     "Draco": houses[3],
#     "Voldemort": houses[3],
#     "Credric": houses[2],
# }


# for student in students:
#     print(student, students[student],sep=": ")

house = ["Gryffindor", "Slytherin"]

students = [
    {"name": "Hermione", "House": house[0], "Patronus": "Otter"},
    {"name": "Harry", "House": house[0], "Patronus": "Stag"},
    {"name": "Ron", "House": house[0], "Patronus": "Jack Russel Terrier"},
    {"name": "Draco", "House": house[1], "Patronus": None},
]

for student in students:
    print(student["name"], student["House"], student["Patronus"], sep=", ")
