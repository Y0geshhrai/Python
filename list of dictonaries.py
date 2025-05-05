#list
#variables (students)
students = [
    {"name": "yogs", "house": "KTM", "patronus": "shhh"},
    {"name": "khaling", "house": "ghattekulo", "patronus": "jjjj"},
    {"name": "rai", "house": "KTM", "patronus": None}
#None = absence of value
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")