info = list(map(int, input().split()))
lst = [0]*info[0]

for i in range(info[1]):
    num_range = list(map(int, input().split()))

    for j in range(num_range[0],num_range[1]+1):
        lst[j-1] = num_range[2]
print(" ".join(list(map(str,lst))))

    
    