while r !=0:
    ladder[r][c] = 0
    if c - 1 >= 0 and ladder[r][c-1] ==1:
        c -= 1
    if c+1 < 100 and ladder[r][c+1] ==1:
        c += 1
    else:
        r -= 1
print(c)