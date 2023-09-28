import sys
from collections import deque

testNum = int(sys.stdin.readline())

for i in range(testNum):
    
    doc_info = list(map(int,sys.stdin.readline().split()))
    importance = deque(map(int, sys.stdin.readline().split()))
    
    ans = sorted(importance.copy(),reverse=True)
    idx = deque(range(0,doc_info[0]))

    i = 0
    while True:
        if (list(importance) == ans) or (doc_info[0] == 1):
            break
        if importance[i] != max(list(importance)[i:]):
            importance.append(importance[i])
            idx.append(idx[i])
            del importance[i]
            del idx[i]
        else:
            i+=1

        
    print(idx.index(doc_info[1])+1)
        

