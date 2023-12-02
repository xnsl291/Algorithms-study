import sys

num, length = map(int,sys.stdin.readline().split())
answer = 0 
max_num = 1001
# lst  = list( map(int,sys.stdin.readline().split()))
lst = [False] * max_num
for i in map(int, input().split()):
    lst[i] = True

x = 0 
while x < max_num:
    if lst[x] :
        answer += 1
        x += length
    else:
        x += 1 

print(answer)