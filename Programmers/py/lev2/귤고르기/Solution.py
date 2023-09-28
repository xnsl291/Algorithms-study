from collections import Counter
def solution(k, tangerine):
    cnt = 0 
    
    dic = dict()
    for i in tangerine:
        dic[i] = dic.get(i,0)+1
    lst = sorted(dic.values() , reverse =True)
    # lst = sorted(Counter(tangerine).values(),reverse=True)
    
    i = 0 
    while(k > 0):
        k -= lst[i]
        cnt += 1
        i+=1
    
    return cnt
