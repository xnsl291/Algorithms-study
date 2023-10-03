def solution(s, skip, index):
    dic = {}
    for string in set(s):
        i = ord(string)
        idx = index
        while idx > 0:
            i += 1
            i -= 26 if i > 122 else 0
            
            idx -= 1 if chr(i) not in skip else 0
        
        dic[string] = chr(i) 
    
    return "".join( [dic[i] for i in s] )


# 다른사람 풀이
from string import ascii_lowercase
# set에서 skip에 포함된 문자 제거 후 index더하여 계산

def solution(s, skip, index):
    result = ''
    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result