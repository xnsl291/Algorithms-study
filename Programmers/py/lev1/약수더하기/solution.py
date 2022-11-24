def solution(n):
    ans_list = [i for i in range(1,n+1) if n%i ==0 ] 
    
    return sum(ans_list)
