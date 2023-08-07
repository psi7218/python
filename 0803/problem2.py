Test_case =int(input())

for case in range(Test_case):
    R,A,B = list(map(int, input().split()))
    l = 1

    A_list= []
    count = 0
    def func1(low, high, answer):
        global count
        F = int((low+high)/2)
        if answer > F:
            count += 1 
            return func1(F, high, answer)
        elif answer < F: 
            count += 1
            return func1(low,F,answer)
        elif F == answer:
            count +=1
            return A_list.append(count)
        
    count2 = 0
    def func2(low, high, answer):
        global count2
        F = int((low+high)/2)
        if answer > F:
            count2 += 1 
            return func2(F, high, answer)
        elif answer < F: 
            count2 += 1
            return func2(low,F,answer)
        elif F == answer:
            count2 +=1
            return A_list.append(count2)   

    
    func1(l,R,A)
    func2(l,R,B)
    print(A_list)
    if A_list[0] < A_list[1]:
        print(f'#{case+1} A')
    elif A_list[0] > A_list[1]:
        print(f'#{case+1} B')
    elif A_list[0] == A_list[1]:
        print(f'#{case+1} 0')
    
    