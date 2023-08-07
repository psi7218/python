N = 5
arr = [[0] * N for _ in range(N)]

num = 1
for r in range(N):
    for c in range(r+1,N):
        arr[r][c] = 1

for line in arr:
    print(*line)

'''
0 1 1 1 1
0 0 1 1 1
0 0 0 1 1
0 0 0 0 1
0 0 0 0 0
'''

N = 5
arr = [[0] * N for _ in range(N)]

num = 1
for r in range(N):
    for c in range(r):
        arr[r][c] = 1

for line in arr:
    print(*line)

'''
0 0 0 0 0
1 0 0 0 0
1 1 0 0 0
1 1 1 0 0
1 1 1 1 0
'''