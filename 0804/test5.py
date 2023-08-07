arr = [[7, 4, 1], [8, 5, 2], [9, 6, 3], 
       [9, 8, 7], [6, 5, 4], [3, 2, 1], 
       [3, 6, 9], [2, 5, 8], [1, 4, 7]]



for m in range(3):
    for n in range(3):
        if m < n:
           arr[m][n],arr[n][m] =arr[n][m],arr[m][n]

print(arr)