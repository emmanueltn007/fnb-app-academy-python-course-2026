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

print("\n --- Student Report ---")

for i, student in enumerate(students, start = 1):
    average_mark = round((student["Mathematics"] + student["Accounting"] + student["Economics"]) / 3)
    
    print(f"{i}. {student['full_name']}")
    
    print(f"   Average %: {average_mark}")
    
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
    
print("\n --- Class Report ---")

#  Build a results list of dictionaries containing: name, average, grade, status

# After the main loop, calculate: class average, highest mark, lowest mark

# Display a formatted class report showing individual results and class statistics

# Use a while loop to let the user search for a student by name after the report is shown

