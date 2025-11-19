import sys

if len(sys.argv) != 5:
    print("Usage: python student_details.py <name> <USN> <department> <semester>")
    sys.exit()

student_name = sys.argv[1]
USN = sys.argv[2]
department = sys.argv[3]
semester = sys.argv[4]

print("Student Details Program")


valid_student_name = "xyz"
valid_USN = "01FE23BCA021"
valid_department = "bca"
valid_semester = "3"


if (student_name == valid_student_name and
    USN == valid_USN and
    department == valid_department and
    semester == valid_semester):
    
    print("Student details are VALID")
else:
    print("Enter valid student details")


