def solution(n):
    lst = [0,1]
    for i in range(1,n):
        lst.append(lst[i-1]+lst[i])
    return lst[n]%1234567
