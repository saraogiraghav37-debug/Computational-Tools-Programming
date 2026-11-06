#Student marks calculation using file handling

file = open("Auxiliary_Files/students.txt","r")
output = open("Auxiliary_Files/result.txt","w")

for line in file:
    data = line.strip().split(",")
    name = data[0]
    marks = list(map(int,data[1:]))
    total = sum(marks)
    avg = total/len(marks)

    #Calculate Grade
    if avg>=90:
        grade="A"
    if avg>=80:
        grade="B"
    if avg>=70:
        grade="C"
    if avg>=60:
        grade="D"
    else: 
        grade = "F"
    result = (f"Name:{name},Total:{total},"
              f"Average:{avg:.2f},Grade:{grade}\n"
    )
    print(result)
    output.write(result)
file.close()
output.close()
print("Results saved in result.txt")