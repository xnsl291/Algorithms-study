def solution(n):
    num_lst = [1 for i in range(2,n+1)] #2~n 
    
    for i in range(2,n):
        for j in range(i,n+1):
            idx = i*j
            if idx > n:
                break
            num_lst[idx - 2] = 0 
            
    return sum(num_lst)


# 다른사람 풀이 
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i)) # 배수 제거 
    return len(num)