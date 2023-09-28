from collections import Counter
string = input().upper()

def get_max(dic):
    cnt = 0 
    lst = []
    for key,val in dic.items():
        if max(dic.values()) == val:
            cnt+=1
            lst.append(key)
    return lst
        
tmp_dic = Counter(string)
result = get_max(tmp_dic)
if len(result) == 1:
    print(result[0])
else:
    print("?")
