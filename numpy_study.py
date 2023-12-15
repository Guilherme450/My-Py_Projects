import numpy as np

A = np.zeros((9, 4))
B = np.zeros((7,4))

data_a = []
data_b = []

for i in range(1, A.shape[0] + 1):
    for j in range(1, A.shape[1] + 1):
        data = (i - j) / (2 * j)
        data_a.append(data)

for i in range(1, B.shape[0] + 1):
    for j in range(1, B.shape[1] + 1):
        data = j - i
        data_b.append(data)

arr_a = np.array([data_a], dtype='float')
arr_b = np.array([data_b], dtype='float')
A_main = arr_a.reshape(9,4)
B_main = arr_b.reshape(7,4).T

C_main = np.matmul(A_main, B_main)

print(C_main[8,5])