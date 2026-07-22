# Practical Task

students = [
    {"full_name": "Thembelihle Notyhawe", "Mathematics": 66, "Accounting": 69, "Economics": 79},
    {"full_name": "Jean Van De Merwe", "Mathematics": 78, "Accounting": 63, "Economics": 78},
    {"full_name": "Sthembiso Mazibuko", "Mathematics": 55, "Accounting": 63, "Economics": 92},
    {"full_name": "Lauretta Mokone", "Mathematics": 43, "Accounting": 56, "Economics": 85},
    {"full_name": "Ntando Mazibuko", "Mathematics": 57, "Accounting": 61, "Economics": 67},
    {"full_name": "John Dow", "Mathematics": 78, "Accounting": 86, "Economics": 65},
    {"full_name": "Leonardo Da Vinci", "Mathematics": 90, "Accounting": 78, "Economics": 76}
]

results = []

def student_results(name, average_mark, grade, status):
    results.append({"name": name, "average": average_mark, "grade": grade, "status": status})
    
def search_student(name):
    for student in students:
        average_mark = round((student["Mathematics"] + student["Accounting"] + student["Economics"]) / 3)
        
        if student["full_name"] == name:
            print(f"{student['full_name']}")
            print(f"Accounting: {student['Accounting']}%")
            print(f"Economics: {student['Economics']}%")
            print(f"Mathematics: {student['Mathematics']}%")
            print(f"Average: {average_mark}%")
            return
    print(f"{name} not found, please try another name.")

print("\n --- STUDENT REPORT ---")

print("--" * 25)

for i, student in enumerate(students, start = 1):
    average_mark = round((student["Mathematics"] + student["Accounting"] + student["Economics"]) / 3)
    
    print(f"{i}. Student full name: {student['full_name']}")
    print(f"   Accounting: {student['Accounting']}%")
    print(f"   Economics: {student['Economics']}%")
    print(f"   Mathematics: {student['Mathematics']}%")
    print(f"   Average: {average_mark}%")
    
    grade = ""
    
    status = ""
    
    if average_mark >= 80: 
        grade = "A"
        print(f"   Grade: {grade}")
    elif average_mark >= 70:
        grade = "B"
        print(f"   Grade: {grade}")
    elif average_mark >= 60:
        grade = "C"
        print(f"   Grade: {grade}")
    elif average_mark >= 50:
        grade = "D"
        print(f"   Grade: {grade}")
    else:
        grade = "F"
        print(f"   Grade: {grade}")
        
    if average_mark < 40:
        status = "Failed"
        print(f"   Status: {status}")
    else: 
        status = "Passed"
        print(f"   Status: {status}")
        
    print("--" * 25)
    
    name = student["full_name"]
    
    student_results(name, average_mark, grade, status)
    
print("\n --- CLASS REPORT ---")

print("--" * 25)

class_average = round(sum(r["average"] for r in results) / len(results))

highest_mark = max(results, key = lambda r: r["average"])

lowest_mark = min(results, key = lambda r: r["average"])

print(f"Class average: {class_average}%")
print(f"Highest mark: {highest_mark['name']} with {highest_mark['average']}%")
print(f"Lowest mark: {lowest_mark['name']} with {lowest_mark['average']}%")

while True:
    choice = input("Do you want to search for a specific student (y/n) ? ").lower().strip()
    
    if choice == "y":
        student_to_search = input("Enter student full name to search: ").title()
        
        search_student(student_to_search)
    else: 
        break

