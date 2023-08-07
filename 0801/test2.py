## 리스트 중 가장 많은 빈도수의 숫자를 찾기 (dict를 사용)
A = [0,4,1,3,1,2,4,1]

cnt_dict = {}
for key in A:
    if key in cnt_dict:
        cnt_dict[key] = cnt_dict[key] +1
    else:
        cnt_dict[key] = 1

print(cnt_dict)


## 카운팅을 하기 위해 자료값을 배열(=list)의 인덱스로 사용
A = [0,4,1,3,1,2,4,1]

C = [0] * 5 # 포함된 요소중 가장 큰 값 +1 
for val in A:
    C[val] += 1

print(C)

