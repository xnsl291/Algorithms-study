def solution(lines):
    min_val = min(lines[0][0],lines[1][0],lines[2][0])
    max_val = max(lines[0][1],lines[1][1],lines[2][1])
    answer = 0
    
    for i in range(min_val, max_val+1):
        cnt = 0 
        
        for j in range(3):
            if lines[j][0] <= i < lines[j][1] :
                cnt+=1
                
        answer += (1 if cnt >=2 else 0)
        
    return answer



# 다른사람 풀이 1
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
# 다른사람 풀이 2
def solution(lines):
    starts = [min(a) for a in lines]
    ends = [max(a) for a in lines]
    starts.sort()
    ends.sort()
    answer = 0
    answer += max(0,ends[0] - starts[1])
    answer += max(0, ends[1] - starts[2])
    answer -= max(0, ends[0] - starts[2])
    return answer