N = int(input())
num_list = list(map(int, input().split()))

count_list = []
count = 1
for i in range(0,len(num_list)-1):
    if num_list[i+1] - num_list[i] ==1:
        count+=1
    else:
        count_list.append(count)
        count = 1
    count_list.append(count)

max_v = count_list[0]
for j in count_list:
    if max_v < j:
        max_v = j
print(max_v)

