arr = [64,25,10,22,11]

N = len(arr)
min_idx = 0
for i in range(1, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
arr[0], arr[min_idx] = arr[min_idx], arr[0]
print(arr)




# 1번부터 N-1번에서 최소값을 찾기
min_idx = 1
for i in range(2, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
arr[1], arr[min_idx] = arr[min_idx], arr[1]
print(arr)



min_idx = 2
for i in range(3, N):
    if arr[min_idx] > arr[i]:
        min_idx = i
arr[2], arr[min_idx] = arr[min_idx], arr[2]
print(arr)


arr = [64,25,10,22,11]

N= len(arr)
for s in range(0, N-1):
    min_idx = s
    for i in range(s+1, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
    arr[s], arr[min_idx] = arr[min_idx], arr[s]
print(arr)