import sys
time = int(sys.stdin.readline())

for i in range(time):
    input= list(map(int,sys.stdin.readline().split()))
    print(input[0]+input[1])
