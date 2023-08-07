Test_case = int(input())

for i in range(Test_case):
    card_count = int(input())
    number = list(map(int, input()))  # 정수열을 각 자리수 마다 리스트에 저장해주는 방식

    max_val = number[0]                        # number
    for val in number:                         # [4, 9, 6, 7, 9]
        if max_val < val:                      # [0, 8, 2, 7, 1]
            max_val = val                      # [7, 7, 9, 7, 9, 4, 6, 5, 4, 3]

    Zero_list = [0] * (max_val+1)
    for j in range(0, card_count):
        Zero_list[number[j]] +=1           # Zero_list
                                           # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]
                                           # [1, 1, 1, 0, 0, 0, 0, 1, 1]
                                           # [0, 0, 0, 1, 2, 1, 1, 3, 0, 2]
    max_idx = 0             
    for k in range(1, len(Zero_list)):
        if Zero_list[max_idx] <= Zero_list[k]:
            max_idx = k


    print(f'#{i+1} {max_idx} {max_val2}')