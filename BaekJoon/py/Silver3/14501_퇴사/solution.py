import sys
from itertools import combinations
num = int(sys.stdin.readline())

schedule = [list(map(int,sys.stdin.readline().split())) for i in range(num)]
dp =[0] * (num+1)

for i in range(len(schedule)):
    for j in range(i + schedule[i][0], len(schedule)+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
            
print(dp[-1])


