def solution(priorities, location):
    queue = [(i,v) for i,v in enumerate(priorities)]
    cnt = 0
    
    while True:
        idx = queue.pop(0) #(0,1)
        
        if any(idx[1] < q[1] for q in queue):
            queue.append(idx)    
        else:
            cnt+=1
            if idx[0] == location:
                return cnt
    
    
    
# p = [1, 3, 9, 1, 1, 1]
# loc = 1
# print(solution(p,loc))



