def solution(rsp):
    dictionary = {"2" : "0", "0":"5" , "5":"2"}
    answer = ''
    for s in rsp:
        answer += dictionary[s]
    return answer