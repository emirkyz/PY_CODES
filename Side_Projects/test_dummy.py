import numpy as np

a = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

a[1, 2] = a[2,1]    # row swapping For anybody else confused about the notation a[[0, 2]]
                    #is shorthand for a[[0, 2], :] so this selects the submatrix consisting of all of rows 0 and 2. 
                    # To interchange columns, you would use a[:, [0, 2]] = a[:, [2, 0]]
print(a)