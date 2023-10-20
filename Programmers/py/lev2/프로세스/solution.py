from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    order = 0
    while queue:
        max_val = max(queue)
        left_val = queue.popleft()
        location -= 1 

        if left_val != max_val:
            queue.append(left_val)
            if location < 0:
                location = len(queue) -1
        else:
            order += 1
            if location < 0:
                break
            
    return order



## 다른사람 풀이 
def solution1(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer