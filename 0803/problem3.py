Test_case = int(input())
 
for case in range(Test_case):
    N = int(input())
    num_list = list(map(int, input().split()))
 
    for i in range(0,N-1):
        for j in range(i+1,N):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    data= ' '.join(map(str,num_list))
    print(f'#{case+1} {data}')