def count_time( string, dic): 
    answer = 0 
    try:
        for s in string :
            answer += dic[s] 
        return answer 
    except:
        
        return -1
    
def solution(keymap, targets):
    dic = dict()  

    for i in keymap:
        for idx, key in enumerate(i):
            value = idx+1
            
            if key in list(dic.keys()):
                dic[key] = dic.get(key) if dic.get(key)<value else value
            else:
                dic[key] = value

    return [ count_time( i , dic) for i in targets ]

# TEST 
# keymap =["AGZ", "BSSS"]
# target = 		["ASA","BGZ"]

# keymap =["AA"]
# target = 		["B"]

# keymap =["ABACD", "BCEFD"]
# target = 	["ABCD","AABB"]
# print(solution(keymap,target))
