# solution 1 : Counter module 사용
from collections import Counter
def solution1(string):
    dic = Counter((string))
    idx_lst = [string.index(val) for val,cnt in dic.items() if cnt == 1] 

    return -1 if len(idx_lst)==0 else min(idx_lst)

# solution2 : dict 사용
def solution2(string):
    dic = dict()
    
    for s in string:
        dic[s] = dic.get(s,0)+1
    
    # 이하동일
    idx_lst = [string.index(val) for val,cnt in dic.items() if cnt == 1] 
    return -1 if len(idx_lst)==0 else min(idx_lst)



string = "abcdeabcdfg"
print(solution1(string))
print(solution2(string))