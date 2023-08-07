Test_case = int(input())

for i in range(Test_case):    
    N = int(input())
    a_list = list(map(int, input().split()))

    count_list = []
    for j in range(0,N-1):
        count = 0
        for k in range(j+1,N):       
            if a_list[j] <= a_list[k]:
                count+=1
        count_list.append(count)    
    
    result_list = []
    for l in range(len(count_list)):
        result = N - (l+1) - count_list[l]
        result_list.append(result)

    max_val = result_list[0]
    for m in result_list:
        if max_val < m:
            max_val = m
        
    print(f'#{i+1} {max_val}')
