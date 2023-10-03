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