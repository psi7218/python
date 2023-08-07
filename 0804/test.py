arr = [[1,2,3,],
       [4,5,6,],
       [7,8,9,]]


for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

arr_90 = []
for k in range(3):
    arr_90.append(arr[k][::-1])

data= ' '.join(map(str, arr_90))
data1=''.join(map(str, data))
print(arr_90)


for m in range(3):
    for n in range(3):
        if m < n:
            arr_90[m][n], arr_90[n][m] = arr_90[n][m], arr_90[m][n]

arr_180 = []
for l in range(3):
    arr_180.append(arr_90[l][::-1])
print(arr_180)

for p in range(3):
    for q in range(3):
        if p < q:
            arr_180[p][q], arr_180[q][p] = arr_180[q][p], arr_180[p][q]

arr_270 = []
for z in range(3):
    arr_270.append(arr_180[z][::-1])
print(arr_270)

last_list =[]

c_list = []
c_list.append(arr_90)
c_list.append(arr_180)
c_list.append(arr_270)
print(c_list)
