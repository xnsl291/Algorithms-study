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