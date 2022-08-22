def solution(answers):
    a,b,c= list(range(1,6)), list([2,1,2,3,2,4,2,5]) ,list([3,3,1,1,2,2,4,4,5,5])

    a = a*int(len(answers)/len(a))+a[:len(answers)%len(a)]
    b = b*int(len(answers)/len(b))+b[:len(answers)%len(b)]
    c = c*int(len(answers)/len(c))+c[:len(answers)%len(c)]
    
    dic_ = {1:[a,0],2:[b,0],3:[c,0]}

    for i in range(1,4):
        for j in range(len(answers)):
            if answers[j] == dic_[i][0][j]:
                dic_[i][1]+=1
   
    max_list = [ list(dic_.values())[i][1] for i in range(3)]
    return [k for k,v in zip(dic_.keys(),max_list ) if v >= max(max_list)]