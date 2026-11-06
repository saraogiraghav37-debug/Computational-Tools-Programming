#Set operations and tuples

student1 = (101,"Lakshya","CSE")
student2 = (102,"Raghav","CSE")

print("Student Details: ",student1,student2,sep="\n")

#Courses enrolled by students
courses1 = {"Python","Java","Maths","Physics"}
courses2 = {"Python","C++","Maths","Chemistry"}

#Union
print("\nAll Courses: ")
print(courses1.union(courses2))

#Intersection
print("\nCommon Courses")
print(courses1.intersection(courses2))

#Differnce
print("\nCourses only in Student 1: ")
print(courses1.difference(courses2))
print("\nCourses only in Student 2: ")
print(courses2.difference(courses1))
