from collections import Counter
def solution(clothes):
    cnt = 1 
    
    closet = Counter([c[1] for c in clothes ])
    for i in closet: 
        cnt *= (closet[i]+1)
        
    return cnt-1
