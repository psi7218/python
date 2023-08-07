Test_case = int(input())

for i in range(Test_case):
    case = int(input())
    number = list(map(int, input().split()))


    Zero_list = [0] * (101)
    for j in range(0, 1000):
        Zero_list[number[j]] +=1

    max_val = Zero_list[0]
    for k in Zero_list:
        if max_val < k:
            max_val = k
    
    max_idx = 0
    for l in range(1, len(Zero_list)):
        if Zero_list[max_idx] <= Zero_list[l]:
            max_idx = l
        
    print(f'#{i+1} {max_idx}')


