import sys


if len(sys.argv) != 5:
    print("Usage: python student_profile.py <Name> <USN> <Department> <Semester>")
    sys.exit()
student_name = sys.argv[1]
USN = sys.argv[2]
department = sys.argv[3]
semester = sys.argv[4]


print("\n========== STUDENT PROFILE CARD ==========")
print(f"Name       : {student_name}")
print(f"USN        : {USN}")
print(f"Department : {department}")
print(f"Semester   : {semester}")
print("===========================================\n")
