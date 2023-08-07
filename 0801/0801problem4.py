Test_case = int(input())

for i in range(Test_case):
    K,N,M = list(map(int,input().split()))
    stop_location = list(map(int, input().split()))
    stop_location.append(N)

           
    count = 0
    start = 0
    for z in range(200):
        a_list= []
        for j in range(1,K+1):
            if start+j in stop_location:
                a_list.append(start+j)
        
        max_val = a_list[0]
        for k in a_list:
            if max_val < k :
                max_val = k
        count += 1
        start += max_val
        if a_list == []:
            print(f'#{i+1} 0')
            
        if start == stop_location[-1]:
            print(f'#{i+1} {count}')
            break