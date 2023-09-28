# from itertools import combinations

def solution(d, budget):
    d.sort()
    answer = 0
    
    for i in range(len(d),0,-1):
        print(d[:i])
        if sum(d[:i])>budget:
            answer+=1
        else:
            break
    return len(d)-answer



