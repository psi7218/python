T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
   

    arr = [list(map(str, input().split())) for _ in range(N)]

    answer = []
    for i in range(0,N):
        result = []
        for A in range(0,N-M+1):
            for j in range(A,M+A):
                if j <= M:
                    result.append(arr[i][j])
                else:
                    pass
            if result == result[::-1]:
                answer.append(result)
            else:
                result= []
    print(answer)