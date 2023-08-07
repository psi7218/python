Test_case = int(input())

for i in range(Test_case):
    N,M = list(map(int, input().split()))
    arr = []
    for j in range(N):
        arr.append(list(map(int, input().split())))
    

    dk = []
    dl = []
    for v in range(M):
        for w in range(M):
            dk.append(v)
            dl.append(w)

    max_v =0
    for k in range(N):
        for l in range(N):
            s = 0
            for m in range(M**2):
                ni,nj=k+dk[m],l+dl[m]
                if 0<=ni<N and 0<=nj<N:
                    s+= arr[ni][nj]
            if max_v <s:
                max_v = s

    print(f'#{i+1} {max_v}')