def solution(citations):
    answer =0  
    citations.sort(reverse=True)
    for idx, cited_num in enumerate(citations, start=1):
        if cited_num >= idx:
            answer +=1
    return answer 





