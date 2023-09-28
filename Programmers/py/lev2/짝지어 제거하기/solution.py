def solution(s):
    lst = ['0'] 
    for word in s:
        if word == lst[-1]:
            lst.pop()
        else:
            lst.append(word)
            
    return 1 if lst == ['0'] else 0
