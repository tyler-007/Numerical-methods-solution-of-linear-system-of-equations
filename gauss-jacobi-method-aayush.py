# Initialize an empty 3x4 array
array_eqns = []

# Loop through each row
for i in range(3):
    row = []
    # Loop through each column in the current row
    for j in range(4):
        value = float(input(f"Enter value for element at row {i+1}, column {j+1}: "))
        row.append(value)
    array_eqns.append(row)

# Convert the list of lists to a NumPy array for easier manipulation
import numpy as np
#array_eqns = np.array(array_eqns)
'''array_eqns=np.array([[ 4,  1, 3, 17],
 [ 1,  5,  1, 14],
 [ 2, -1, 8, 12]])'''

# Print the resulting array
print("User input array:")
print(array_eqns)

array_x=[]
array_y=[]
array_z=[]

# For iteration creating temp elements
temp_x=0
temp_y=0
temp_z=0

# For finding the number of iteration
iter = int(input("Enter the maximum number of iterations: "))

# Looping them
for i in range(iter):
    x1=(array_eqns[0][3]-(array_eqns[0][1]*temp_y)-(array_eqns[0][2]*temp_z))/array_eqns[0][0]
    array_x.append(x1)
    x2=(array_eqns[1][3]-(array_eqns[1][0]*temp_x)-(array_eqns[1][2]*temp_z))/array_eqns[1][1]
    array_y.append(x2)
    x3=(array_eqns[2][3]-(array_eqns[2][0]*temp_x)-(array_eqns[2][1]*temp_y))/array_eqns[2][2]
    array_z.append(x3)
    temp_z=x3
    temp_y=x2
    temp_x=x1

print(array_x)
print(array_y)
print(array_z)
import matplotlib.pyplot as plt

plt.figure()

# Plot each array as dots (scatter plot) with different colors and labels
plt.scatter(range(len(array_x)), array_x, color='red', label='different iteration values of x')
plt.scatter(range(len(array_y)), array_y, color='blue', label='different iteration values of y')
plt.scatter(range(len(array_z)), array_z, color='green', label='different iteration values of z')
#plt.ylim(min(array_x) - 0.001, max(array_x) + 0.001)  # Adjust the offset as needed


# Add labels and a legend
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Gauss-Jacobi Method')
plt.legend()

# Show the plot
plt.show()
