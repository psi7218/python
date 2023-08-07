T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    
    answer = []
    for i in range(0,N):
        result = []
        for A in range(0,N-M+1):
            for j in range(A,M+A):
                result.append(arr[i][j])

            if result == result[::-1]:
                answer = result
            else:
                result= []

    if answer != []:
        test = ''.join(map(str, answer))
        print(f'#{tc} {test}')
        continue
    elif answer == []:
        for k in range(0,N):
            for l in range(0,N):
                if k<l:
                    arr[k][l], arr[l][k] = arr[l][k], arr[k][l]
        
        for x in range(0,N):
            result1 = []
            for B in range(0,N-M+1):
                for y in range(B,M+B):
                    result1.append(arr[x][y])

                if result1 == result1[::-1]:
                    answer = result1
                else:
                    result1= []
    test = ''.join(map(str, answer))
    print(f'#{tc} {test}')