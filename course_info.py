Room_Numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "CSC241": "1411"
}

Instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "CSC241": "Lee"
}

Meeting_Time = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "CSC241": "1:00 p.m."
}

course_num = input("Enter a course number: ")

if course_num in Room_Numbers:
    print("Room Number: " + Room_Numbers[course_num])
    print("Instructor: " + Instructors[course_num])
    print("Meeting Time: " + Meeting_Time[course_num])
else:
    print("Class Not found")