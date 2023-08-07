Test_case  = int(input())

for case in range(Test_case):
    N = int(input())
    n_list = list(map(int, input().split()))


    num_list = []
    for i in range(5): 
        max_v = n_list[0]
        min_v = n_list[0]
        for j in n_list:
            if max_v < j:
                max_v = j
        num_list.append(max_v)
        n_list.remove(max_v)
        for k in n_list:
            if min_v > k:
                min_v = k
        num_list.append(min_v)
        n_list.remove(min_v)
    data = ' '.join(map(str,num_list))
    
    print(f'#{case+1} {data}')