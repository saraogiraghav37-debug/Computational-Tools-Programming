# Statistical operations with and without NumPy

import numpy as np
import statistics

marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]

sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]


# Without NumPy
def without_numpy(data):
    mean = sum(data) / len(data)
    median = statistics.median(data)

    # Population standard deviation
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5

    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)
    print("Minimum:", min(data))
    print("Maximum:", max(data))


# With NumPy
def with_numpy(data):
    array = np.array(data)

    print("Mean:", np.mean(array))
    print("Median:", np.median(array))
    print("Standard Deviation:", np.std(array))
    print("Minimum:", np.min(array))
    print("Maximum:", np.max(array))


datasets = {
    "Marks": marks,
    "Temperatures": temperatures,
    "Sales": sales
}

for name, data in datasets.items():

    print("\n", name)

    print("\nWithout NumPy:")
    without_numpy(data)

    print("\nWith NumPy:")
    with_numpy(data)