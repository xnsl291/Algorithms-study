def solution(priorities, location):
    
    for i in priorities:
        if i != max(priorities):
            priorities.append(i)
            priorities.pop(0)

    
    return location



p = [1, 1, 9, 1, 1, 1]
l = 0
print(solution(p,l))