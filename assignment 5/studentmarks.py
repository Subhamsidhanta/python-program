students={
    "suresh":99,
    "subham":98,
    "sourav":97,
    "sovon":96,
}
name=input("Enter the student's name : ")
if name in students:
    print(f"{name}'s marks : {students[name]} ")
else:
    print("Student not found")