N = 10 
arr = [[0] * N for _ in range(N)]

r,c = 0,0 # 기준점
arr[r][c] = '*'
dr = [-1,0,1,0]
dc = [0,1,0,-1]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0<=nr<N and 0<=nc<N:
        arr[nr][nc] = i + 1


# arr[r+dr[0]][c+dc[0]] = 1
# arr[r+dr[1]][c+dc[1]] = 2
# arr[r+dr[2]][c+dc[2]] = 3
# arr[r+dr[3]][c+dc[3]] = 4



for line in arr:
    print(*line)