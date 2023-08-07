Test_case = int(input())

for i in range(Test_case):
    N = int(input())
    arr = []
    for j in range(N):
        arr.append(list(map(int, input().split())))

    dk = [0,1,0,-1]
    dl = [1,0,-1,0]

    max_v = 0
    max_v_idx_column = 0
    max_v_idx_row = 0

    for s in range(N):
        for t in range(N):
            me = 0
            for m in range(4):
                ni,nj = s+dk[m],t+dl[m]
                if 0<=ni<N and 0<=nj<N:
                    me += arr[ni][nj]
            if max_v < me:
                max_v = me
                max_v_idx_column =s
                max_v_idx_row =t

    print(f'#{i+1} {max_v_idx_column} {max_v_idx_row} {max_v}')
        