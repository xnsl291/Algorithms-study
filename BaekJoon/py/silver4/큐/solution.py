import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if len(queue)<1 else 0)
    elif command[0] == "pop":
        print( -1 if len(queue)==0 else queue.popleft())
    
    elif command[0] == "front":
        print(-1 if len(queue)<1 else queue[0])
    elif command[0] == "back":
        print(-1 if len(queue)<1 else queue[-1])
    
