Test_case = int(input())

for i in range(Test_case):    
    N = int(input())
    a_list = list(map(int, input().split()))

    result_list= []
    for j in range(len(a_list)-1):
        result = a_list[j] + a_list[j+1]
        result_list.append(result)
    
        max_val = result_list[0]
        for k in result_list:
            if max_val < k:
                max_val =k
    print(f'#{i+1} {max_val}')
            

