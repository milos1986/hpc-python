'''
## Array slicing

First, create a 4x4 array with arbitrary values, then

1. Extract every element from the second row.
2. Extract every element from the third column.
3. Assign a value of 0.21 to upper left 2x2 subarray.

Next, create a 8x8 array with checkerboard pattern, i.e. alternating zeros
and ones:

```
1 0 1 ...
0 1 0 ...
1 0 1 ...
 ...
```
'''
import numpy as np

z = np.empty((4, 4))
print(z)
# 1
print(z[1,:])

# 2
print(z[:,2])

# 3
z[0:2, 0:2] = 0.21
print(z)

# 4
checkerboard = np.zeros((8, 8), dtype = np.int8)
print(checkerboard)

n_rows, n_cols = np.shape(checkerboard)
col_idx = np.arange(start=0, stop=n_cols, step=1, dtype=np.int8)
row_idx = np.arange(start=0, stop=n_rows, step=1, dtype=np.int8)
checkerboard[0:9:2, 0:9:2] = 1
checkerboard[1:9:2, 1:9:2] = 1
# a moze i ovako:
# checker[::2, ::2] = 1
# checker[1::2, 1::2] = 1
print(checkerboard)

import timeit

# vectorised operation
def vect_dif():
    arr = np.arange(1000)
    dif = arr[1:] - arr[:-1]
    return

def non_vect_dif():
    # brute force using a for loop
    arr = np.arange(1000)
    dif = np.zeros(999, int)
    for i in range(1, len(arr)):
        dif[i-1] = arr[i] - arr[i-1]

# in jupyter iPython:
# timeit vect_dif()
# and
# timeit non_vect_dif()