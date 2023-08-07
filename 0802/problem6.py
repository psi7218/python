Test_case = int(input())

for case in range(Test_case):
    K,N,M = list(map(int, input().split()))
    charge_num = list(map(int, input().split()))
    charge_num.append(N)

    for num1 in range(0,len(charge_num)-1):
        if charge_num[num1+1] - charge_num[num1] > K:
                print(f'#{case+1} 0')

    location = 0
    count = 0
    def func():
        global location
        global count            
        for i in range(K,0,-1):
            location += i
            if location == N:
                return print(f'#{case+1} {count}')
            elif location in charge_num:
                count += 1
                return func()
            elif location not in charge_num:
                location -= i
                
    func()

    