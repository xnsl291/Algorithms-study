def solution(elements):
    answer = elements.copy()
    answer.append(sum(elements))

    N = len(elements)
    
    for i in range(2,N):
        total = sum(elements[:i])
        start, end = 0, i
        
        for j in range(N):
            total += elements[end] - elements[start]
            start, end = start+1, (end+1)%N
            answer.append(total)
            
    return len(set(answer))