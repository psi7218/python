Test_case = int(input())

for i in range(Test_case):
    a, b = list(map(int, input().split()))
    num_list = list(map(int, input().split()))


    sum_list = []
    for j in range(a-b+1):
        d_list = num_list[j:j+b]
        sum= 0
        for num in d_list:
            sum += num

        sum_list.append(sum)

    max_val = sum_list[0]
    min_val = sum_list[0]

    for k in sum_list:
        if max_val < k:
            max_val = k
        if min_val > k:
            min_val = k

    print(f'#{i+1} {max_val - min_val}')