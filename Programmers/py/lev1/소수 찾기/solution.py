def solution(n):
    num_lst = [1 for i in range(2,n+1)] #2~n 
    multifly_val = 2 
    
    while(multifly_val <= n):
        for i in range(2,n+1):
            idx = i*multifly_val
            if idx > n:
                break
            num_lst[idx - 2] = 0 
        multifly_val +=1 
            
    return sum(num_lst)
