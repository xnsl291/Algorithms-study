import sys

n = int(sys.stdin.readline())
answer = []
for i in range(n):
    input = int(sys.stdin.readline())
    answer.append(input) if input!=0 else answer.pop()
print(sum(answer))


