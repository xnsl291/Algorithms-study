def solution(answer):
    p1 = [1,2,3,4,5]
    p2 = [1,3,4,5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0]*3
    
    for idx, val in enumerate(answer):
        score[0] +=  1 if val == p1[idx % len(p1)] else 0
        score[1] += 1 if (idx%2 > 0 and (val == p2[idx//2 % len(p2)] == val) ) else 1 if (idx%2 == 0 and val == 2) else 0  
        score[2] += 1 if val == p3[idx % lden(p3)] else 0
    
    max_val = max(score)
    if score.count(max_val) > 1 : 
        return [i+1 for i in range(3) if score[i] == max_val]
    return [score.index(max(score))+1]