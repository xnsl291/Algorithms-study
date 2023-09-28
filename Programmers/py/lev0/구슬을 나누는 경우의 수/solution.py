# 간단 버전
import math
def solution(balls, share):
    return math.comb(balls,share)

# 구현
def solution(balls, share):
    parent,child = 1,1
    share = max(share, balls-share)
    
    for i in range(share+1,balls+1):
        parent*=i
    for i in range(1,balls-share+1):
        child *= i 
        
    return int(parent/child)