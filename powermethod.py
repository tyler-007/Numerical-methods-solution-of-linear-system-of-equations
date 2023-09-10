#finding largest eigen value using power method.
iterations=int(input("enter the value of number of iterations you want: "))
A = []
max_value_array=[]

for i in range(3):
    row = []
    # Loop through each column in the current row
    for j in range(3):
        value = float(input(f"Enter value for element at row {i+1}, column {j+1}: "))
        row.append(value)
    A.append(row)
import numpy as np
#intilaize 
xo=[1,0,0]
#under loop- 
for i in range (0,iterations):
    result = np.dot(A, xo)
    max_value = np.max(result)
    max_value_array.append(max_value)
    xo=(result/max_value)

import matplotlib.pyplot as plt

plt.plot(max_value_array, marker='o',label='Change in values of Eigen Values')
plt.xlabel('Eigen Values')
plt.title('Power Method')
plt.legend()

# Show the plot
plt.show()


