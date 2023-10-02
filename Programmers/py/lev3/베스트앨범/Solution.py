def solution(genres, plays): 
    answer = [] 
    genre_dic = { i : [] for i in set(genres)}
    
    for i in range(len(genres)):
        genre_dic[ genres[i]  ].append([plays[i],i])
    # genre_dic에 장르별로 재생수&index 저장 
    # [결과] genre_dic => {'classic': [[500, 0], [150, 2], [800, 3]], 'pop': [[600, 1], [2500, 4]]}
    
    sum_lst = sorted([ [sum([x[0] for x in genre_dic[val]]) , val]  for val in  genre_dic.keys() ] ,reverse=True)
    #sum_lst = 장르별 총 재생수
    # [결과] sum_lst => [[3100, 'pop'], [1450, 'classic']]
    
    for val in sum_lst: 
        genre_dic[val[1]] = sorted(genre_dic[val[1]] ,key = lambda x : (-x[0],x[1]))[:2]
        for i in genre_dic[val[1]] :
            answer.append(i[1])
    # 총 재생수 많은 장르부터 answer에 추가 
    return answer
    
        