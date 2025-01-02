def solution(n):
    cnt=0 
    while(n>0):
        cnt+=1 if n%2==1 else 0
        n//=2
    return cnt