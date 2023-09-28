def solution(dot):
    if dot[0]>0 :
        return 1 if dot[1]>0 else 4
    elif dot[0]<0:
        return 2 if dot[1]>0 else 3
    
# 다른사람 풀이
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
