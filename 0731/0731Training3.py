Test_case = 10

for i in range(Test_case):
    N = int(input())   # 100
    arr = list(map(int, input().split()))

    sum = 0
    for j in range(2,N-2):
        case1 = arr[j] - arr[j-2]
        case2 = arr[j] - arr[j-1]
        case3 = arr[j] - arr[j+1]
        case4 = arr[j] - arr[j+2]
        case_list = [case1,case2,case3,case4]
               
        min_val = case_list[0]
        for k in case_list:
            if min_val > k:
                min_val = k           
        
        if min_val <= 0:
            min_val = 0
        else:
            sum += min_val

    print(f'#{i+1} {sum}')





