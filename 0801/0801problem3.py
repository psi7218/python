for i in range(10):
    dump_count = int(input())
    height_list = list(map(int, input().split()))

    for j in range(dump_count):   # 834
        max_idx= 0
        min_idx= 0
        for k in range(1, len(height_list)):
            if height_list[max_idx] < height_list[k]:
                max_idx = k
            if height_list[min_idx] > height_list[k]:
                min_idx = k

        if (height_list[max_idx] - height_list[min_idx]) == 0 or (height_list[max_idx] - height_list[min_idx]) ==1:
            break
        else:
            height_list[max_idx] -= 1
            height_list[min_idx] += 1

    max_idx= 0
    min_idx= 0
    for k in range(1, len(height_list)):
        if height_list[max_idx] < height_list[k]:
            max_idx = k
        if height_list[min_idx] > height_list[k]:
            min_idx = k
    
        
    print(f'#{i+1} {height_list[max_idx] - height_list[min_idx]}')