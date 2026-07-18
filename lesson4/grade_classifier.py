# Practical Task

student_name = input("Enter your full name: ").upper()
subject1_mark = float(input("Enter your first subject's mark: "))
subject2_mark = float(input("Enter your second subject's mark: "))
subject3_mark = float(input("Enter your third subject's mark: "))

average_mark = (subject1_mark + subject2_mark + subject3_mark) / 3
    
print(f"Student name: {student_name}") 

print("SUBJECT 1:")

print(f"Mark: {subject1_mark}%")

if subject1_mark < 40:
    print("Needs intervention")
else:
    print("Intervention: None needed")

print("SUBJECT 2:")

print(f"Mark: {subject1_mark}%")

if subject2_mark < 40:
    print("Needs intervention")
else:
    print("Intervention: None needed")

print("SUBJECT 3:")

print(f"Mark: {subject1_mark}%")

if subject3_mark < 40:
    print("Intervention: Needs intervention")
else:
    print("Intervention: None needed")

print(f"Average mark: {round(average_mark)}")

if average_mark < 40:
    print("FAIL")
else: 
    print("PASS")

if average_mark >= 80:
    print("Grade: A")
elif average_mark >= 70:
    print("Grade: B")
elif average_mark >= 60:
    print("Grade: C")
elif average_mark >= 50:
    print("Grade: D")
else:
    print("Grade: F")
