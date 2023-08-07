import sys
sys.stdin = open("123123.txt")

for case in range(10):
    N = int(input())
    A_list = []
    for k in range(100):
        A_list.append(list(map(int, input().split())))
    
    for i in range(100):
        for j in range(100):
            if A_list[i][j] ==2:
                a=i
                b=j
   
   
    def func(a,b):
        if a >99 or a<0 or b>99 or b<0:
            continue
        elif 
            A_list[a][b] += 5
            return func(a-1,b)
        elif 
        elif a==0:
            print(f'#{case+1} {b}')


    func(a,b)
