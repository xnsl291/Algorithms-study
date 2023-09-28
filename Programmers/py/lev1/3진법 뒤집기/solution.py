def solution(n):
    result , target = 0, 3
    lst = []
    # 3진법 구화기 
    while(n > target-1):
        lst.append( n%target )
        n = n//3
    lst.append(n)
    print(lst)
    # 10 진법으로 변경
    for i in range(len(lst)):
        result += (lst[i] * pow( target , len(lst)-i-1   ) )
    
    # return sum(lst)
    return result


print("resiult : ",solution(45))