def solution(ingredient):
    lst = [] 
    cnt = 0
    
    for i in ingredient : 
        lst.append(i)
        
        if lst[-4:] == [1,2,3,1]:
            cnt+=1
            # lst = lst[:-4]
            for _ in range(4):
                lst.pop()
    return cnt