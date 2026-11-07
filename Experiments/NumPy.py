# Student marks analysis using NumPy

import numpy as np

students = ["S1", "S2", "S3", "S4", "S5"]

subjects = ["Mathematics", "Physics", "Chemistry", "English"]

# Mid-semester marks
mid_marks = np.array([
    [65, 70, 68, 72],
    [78, 75, 80, 77],
    [55, 60, 58, 62],
    [82, 85, 80, 88],
    [70, 68, 72, 74]
])

# End-semester marks
end_marks = np.array([
    [72, 78, 75, 80],
    [84, 82, 86, 83],
    [65, 68, 66, 70],
    [88, 90, 85, 92],
    [78, 75, 80, 82]
])

# Calculate total marks
total = np.sum(end_marks, axis=1)

# Calculate average marks
average = np.mean(end_marks, axis=1)

# Calculate percentage improvement
mid_total = np.sum(mid_marks, axis=1)

improvement = ((total - mid_total) / mid_total) * 100

# Display results
print("Student  Total  Average  Improvement")

for i in range(len(students)):
    print(
        students[i],
        total[i],
        average[i],
        round(improvement[i], 2), "%"
    )