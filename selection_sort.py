# -*- coding: utf-8 -*-
"""Selection Sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b8IwrlFMN1voA6F_EUYDaMhkAnrajR6e
"""

import numpy as np
import time

def viraj_selection_sort(list):
    for i in range(len(list)):
        min=i
        for j in range (i+1, len(list)):
            if list[min] > list[i]:
                min=j

# Apply swapping formula
        list[i], list[min] = list[min], list[i]
    return list

n = int(input("Enter length of an array: "))
list = np.random.randint(1,1000,n)

print("Unsorted list is: ", list)
print("-------------------------------------------------------------------------------------------------")

start = time.time()
print("Sorted list is:", viraj_selection_sort(list))
print("-------------------------------------------------------------------------------------------------")

end = time.time()
print("Runtime for Selection Sort is:", end - start, "seconds")

import matplotlib.pyplot as plt
 # Example data
input_sizes = [5, 50, 100, 500, 1000]
# Replace with your input sizes
execution_times = [0.0004, 0.006, 0.0059, 0.034, 0.138]
# Replace with your measured times
# Create the plot
plt.plot(input_sizes, execution_times, marker='o', linestyle='-')
 # Label the axes and add a title
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Benchmark')
# Display the plot
plt.grid(True)
plt.show()

