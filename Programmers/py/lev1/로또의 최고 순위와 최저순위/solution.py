def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    num = len([ i for i in lottos if i in win_nums  ])
    
    return [rank[num+lottos.count(0)] , rank[num] ]