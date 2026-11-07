#Student record management using lists and dictionaries

students = [{"roll": 101, "name": "Lakshyajit", "department": "CSE"},
            {"roll": 102, "name": "Raghav", "department": "CSE"},
            {"roll": 103, "name": "Raveendra", "department": "CSE"}]
def insert():
    roll = int(input("Enter roll no: "))
    name = input("Enter your name: ")
    dept = input("Enter department: ")
    students.append({"roll": roll, "name": name, "department": dept})
    print("Student added successfuly")

def delete():
    roll = int(input("Enter roll no to delete: "))
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfuly")
            return
    print("Student not found")

def search():
    roll = int(input("Enter roll no to search: "))
    for student in students:
            if student["roll"] == roll:
                print("Student details: ",student)
                return
    print("Student not found")

def display():
    for student in students:
        print(student)

#Main Program
while True:
    print("\n1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))
    if(choice==1):
        insert()
    elif(choice==2):
        delete()
    elif choice==3:
        search()
    elif choice==4:
        display()
    elif choice==5:
        break
    else: 
        print("Invalid Choice!")