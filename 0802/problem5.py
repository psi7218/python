for i in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []
    for j in range(100):
        sum_list.append(sum(arr[j]))

    
    for k in range(100):
        for l in range(100):
            if k < l:
                arr[k][l], arr[l][k] = arr[l][k], arr[k][l]
    
    for m in range(100):
        sum_list.append(sum(arr[m]))

    sum1= 0
    for n in range(100):
        for o in range(100):
            if n==o:
                sum1+= arr[n][o]        
    sum_list.append(sum1)

    sum2=0
    for p in range(100):
        for q in range(100):
            if p+q == 99:
                sum2+= arr[p][q]
    sum_list.append(sum2)

    print(f'#{i+1} {max(sum_list)}')