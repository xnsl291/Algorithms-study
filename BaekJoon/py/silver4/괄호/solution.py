num = int(input())

for i in range(num):
    lst = list(input())
    cnt = 0
    for j in lst:
        cnt = cnt+1 if j == '(' else cnt-1 if  j == ')' else cnt
            
        if cnt < 0:
            print('NO')
            break
        
    if cnt==0:
        print('YES')
    elif cnt >0:
        print("NO")
        