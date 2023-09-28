n = int(input())
num_lst = list(map(int,input().split()))
target = int(input())

print(sum([1 for i in num_lst if i == target]))

