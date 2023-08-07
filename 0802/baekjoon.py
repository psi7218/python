for case in range(4):
    N = int(input())
    if N == -1:
        break

    num_list = []
    for i in range(1,N):
        if N % i == 0:
            num_list.append(i)
    
    num_sum = 0
    for j in num_list:
        num_sum += j
    
    
    

    if num_sum == N:
        print(f'{N} = ')
    else:
        print(f'{N} is NOT perfect')