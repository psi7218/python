Test_case = int(input())

for i in range(Test_case):
    K,N,M = list(map(int,input().split()))
    stop_location = list(map(int, input().split()))
    stop_location.append(N)

    print(stop_location)
   