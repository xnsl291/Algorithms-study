num = list(map(int, input().split()))
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[:num[2]-1])

