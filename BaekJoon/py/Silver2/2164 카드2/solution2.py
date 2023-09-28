#solution2 - queue
from collections import deque
import sys
lst = deque(range(1,int(sys.stdin.readline())+1))
if len(lst)>1:
    while(True):
        lst.popleft()
        lst.append(lst[0])
        lst.popleft()

        if len(lst)==1:
            break


print(lst[0])
