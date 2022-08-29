def solution(n):
    cnt = 0
    for i in range(1,n+1):
        if len([j for j in range(1,i+1) if i % j ==0]) == 2:
            cnt+=1
    return cnt