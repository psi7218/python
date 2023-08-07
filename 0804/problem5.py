Test_case = int(input())

for case in range(1,Test_case+1):
    a,b = map(int, input().split())

    result = a*b
    z_list = [[0] * b] *a
    for i in range(a):
        for j in range(b):
            Array[i][j + (b-1-2*j) * (i%2)]








