num = int(input())

for i in range(num):
    lst = list(input())
    cnt = 0
    for j in lst:
        if j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    print('NO') if cnt > 0 else print('YES')
        