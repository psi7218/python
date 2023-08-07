Test_case = int(input())

for case in range(1,Test_case+1):
    N = int(input())
    a_list = [2,3,5,7,11]

    result =[]
    for a in a_list:
        count=0
        while True:
            N = N/a
            count+=1 
            if N % a !=0:
                break
        result.append(count)

    print(result)
    