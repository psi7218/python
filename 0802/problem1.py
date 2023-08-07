N= int(input())

for x in range(N):
    N,M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    max_v = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<N and 0<=nj<M:
                    s+= arr[ni][nj]
            if max_v <s:
                max_v =s
    print(f'#{x+1} {max_v}')