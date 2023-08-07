Test_case= int(input())

for case in range(1,Test_case+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    check_list = [1,2,3,4,5,6,7,8,9]
    
    score = 0
    # 행 구간 확인
    for i in range(9):
        num_list = []
        for j in range(9):
            num_list.append(arr[i][j])
        count = 0
        for k in check_list:
            if k not in num_list:
                count+= 1
        if count != 0:
            break
        else:
            score += 1

    # 3x3 확인
    a= 0
    b= 3
    c= 0
    d= 3
    for z in range(9):
        count1 = 0
        num1_list =[]
        for l in range(a,b):
            for m in range(c,d):
                num1_list.append(arr[l][m])
        for n in check_list:
            if n not in num1_list:
                count1+= 1
        if count1 != 0:
            break
        else:
            score+=1
        if d != 9:
            c+=3
            d+=3
        else:
            a+= 3
            b+= 3
            c = 0
            d = 3

    # 열 구간 확인
    for x in range(9):
        for y in range(9):
            if x < y:
                arr[x][y],arr[y][x] = arr[y][x] , arr[x][y]

    for p in range(9):
        num2_list = []
        for q in range(9):
            num2_list.append(arr[p][q])
        count2 = 0
        for s in check_list:
            if s not in num2_list:
                count2 += 1
        if count2 != 0:
            break
        else:
            score +=1
    
    if score == 27:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
