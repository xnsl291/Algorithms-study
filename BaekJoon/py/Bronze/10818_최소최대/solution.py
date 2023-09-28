n = int(input())
numbers = list(map(int, input().split(" ")))[:n]

print(min(numbers),max(numbers))