from collections import deque
def solution(people, limit):
    people = deque( sorted(people))
    cnt = 0
   
    while( len(people) > 1):
        weight = people[0] + people[-1]
        
        if weight <= limit:
            people.popleft()
            people.pop()
            
        elif weight > limit:
            people.pop()
        
        cnt+=1
        
        if len(people)==1:
            cnt+=1
            
    return cnt
        
