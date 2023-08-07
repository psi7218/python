a =[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
c = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]


result_list = []
for i in a:
    result_list.append(i)
for j in b:
    result_list.append(j)
for k in c:
    result_list.append(k)    

print(result_list)
real_last_list = []
for l in result_list:
    x =(''.join(map(str,l)))
    real_last_list.append([x])
print(real_last_list)

