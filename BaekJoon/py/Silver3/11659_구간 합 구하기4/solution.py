import sys
n,m = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()[:n]))
total = 0
dp = [0]*(n+1)

# 누적합 배열 
for i in range(1,n+1):
    total += numbers[i-1]
    dp[i] = total
    # dp[i] = dp[i-1] + numbers[i-1]

for i in range(m):
    i,j = map(int,sys.stdin.readline().split())
    print(dp[j] - dp[i-1])
