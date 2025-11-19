import sys


if len(sys.argv) != 5:
    print("Usage: python student_profile.py <student_Name> <USN> <Department> <Semester>")
    sys.exit()


student_name = sys.argv[1]
USN = sys.argv[2]
department = sys.argv[3]
semester = sys.argv[4]

if student_name and USN and department and semester:
    print("\n========== STUDENT PROFILE CARD ==========")
    print(f"Name       : {student_name}")
    print(f"USN        : {USN}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print("===========================================\n")
else:
    print("Invalid input: All fields are required!")
