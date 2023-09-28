def solution(name, yearning, photo):
    dic = dict()
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    return [sum(dic[p_name] for p_name in n_lst if p_name in dic.keys()) for n_lst in photo]

# name = ["may", "kein", "kain", "radi"]
# yearning = [5, 10, 1, 3]
# photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name, yearning, photo))