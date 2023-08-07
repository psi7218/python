Test_case = int(input())

for i in range(Test_case):
    a = int(input())
    num_list = list(map(int, input().split()))

    
    max_val = min_val = num_list[0]
    for j in num_list:
        if max_val < j:
            max_val = j
        if min_val > j:
            min_val = j
    
    print(f'#{i+1} {max_val - min_val}')

