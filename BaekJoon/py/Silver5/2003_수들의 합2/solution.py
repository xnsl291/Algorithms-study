import sys
n,m = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()[:n]))

start, cnt = 0,0
end = start +1
total = numbers[start]

while(True):
    if total < m:
        if end == n:
            break
        total += numbers[end]
        end +=1
        
    else:
        if total == m:
            cnt +=1
        total -= numbers[start]
        start+=1
        
print(cnt)

