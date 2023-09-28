import sys

input_num = int(sys.stdin.readline())

stack = []
result = []
flag = 0 
point = 1

for _ in range(input_num):
    target = int(sys.stdin.readline())

    while point <= target:
        stack.append(point)
        # print("+")
        result.append("+")
        point+=1

    if target == stack[-1]:
        stack.pop()
        # print("-")
        result.append("-")
    else:
        print("NO") 
        flag = 1
        break

if flag != 1 :
    for i in result:
        print(i)




