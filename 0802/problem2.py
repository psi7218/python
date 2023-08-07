
Test_case = int(input())

for i in range(Test_case):
    L = 10 
    arr = [[0] * L for _ in range(L)]
    N = int(input())
    for j in range(N):
        r1,c1,r2,c2,color= list(map(int, input().split()))
    
        for s in range(r1,r2 +1):
            for t in range(c1,c2 +1):
                if arr[s][t] == 0:
                    arr[s][t] = color
                elif arr[s][t] == color:
                    arr[s][t] = color
                elif arr[s][t] != color:
                    arr[s][t] = 3
          

    count = 0         
    for s in range(10):
        for t in range(10):
            if arr[s][t] == 3:
                count +=1
    print(f'#{i+1} {count}')


