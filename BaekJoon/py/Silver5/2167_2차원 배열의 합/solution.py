n,m = map(int,input().split())
numbers = [ list(map(int,input().split()[:m])) for _ in range(n) ]


sum_num = int(input())
dp_arr = [[0] * (m + 1) for _ in range(n + 1)]

# 누적 합
for i in range(1, n + 1):
    for j in range(1, m+1 ):
        dp_arr[i][j] = numbers[i - 1][j - 1] + dp_arr[i - 1][j] + dp_arr[i][j - 1] - dp_arr[i - 1][j - 1]
        
for _ in range(sum_num):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp_arr[x2][y2] - dp_arr[x1 - 1][y2] - dp_arr[x2][y1 - 1] + dp_arr[x1 - 1][y1 - 1])
    