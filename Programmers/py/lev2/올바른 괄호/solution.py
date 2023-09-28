def solution(s):
    s = list(s)
    flag = 0
    cnt = 0
    for idx,i in enumerate(s):
        cnt = cnt+1 if i == "(" else cnt-1
       
        if cnt <0:
            return False
    return cnt ==0 