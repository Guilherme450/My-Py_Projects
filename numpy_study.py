import numpy as np

# Initialize matrices A and B with zeros
A = np.zeros((9, 4))
B = np.zeros((7, 4))

# Lists to store data for matrices A and B
data_a = []
data_b = []

# Fill data for matrix A
for i in range(1, A.shape[0] + 1):
    for j in range(1, A.shape[1] + 1):
        data = (i - j) / (2 * j)
        data_a.append(data)

# Fill data for matrix B
for i in range(1, B.shape[0] + 1):
    for j in range(1, B.shape[1] + 1):
        data = j - i
        data_b.append(data)

# Convert data lists to NumPy arrays
arr_a = np.array([data_a], dtype='float')
arr_b = np.array([data_b], dtype='float')

# Reshape arrays to match matrix dimensions
A_main = arr_a.reshape(9, 4)
B_main = arr_b.reshape(7, 4).T  # Transpose for matrix multiplication compatibility
C_main = np.matmul(A_main, B_main)  # Perform matrix multiplication

# Print the element at position (8, 5) in the result matrix C_main
print(C_main[8, 5])
