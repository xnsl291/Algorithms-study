def solution(emergency):
    sort_lst = sorted(emergency,reverse=True)
    answer = [sort_lst.index(i)+1 for i in emergency]
    return answer


# 다른사람 풀이 : 딕셔너리 활용 
# index쓰면 시간 복잡도가 o(n^2)이기 떄문에 딕셔너리 풀이가 시간복잡도 측면에서 효율적임
def solution(emergency):
    answer = []
    emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
    for e in emergency:
        answer.append(emer_ls[e])
    return answer