import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
num_lst = list(map(int,sys.stdin.readline().split()[:n]))

cnt = 0
num_lst.sort()

start = 0 
end = n-1
# 1 2 3 4 5 7
while(start < end ):
    value = num_lst[start] + num_lst[end]
    if value < m : 
        start += 1
    elif value == m:
        cnt +=1
        start += 1
        end -=1 
    elif value > m :
        end -=1
        

print(cnt)



# 다른사람 풀이 - 천잰가 진짜,, 
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# number = set(map(int, input().split()))
# answer = 0
# for i in number:
#     if m - i in number:
#         answer += 1
# answer = answer // 2
# print(answer)