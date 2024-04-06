def solution(number, k):
    lst = [] 
    for num in number:
        while k > 0 and len(lst)>0 and lst[-1] < num:
            lst.pop()
            k -= 1
        lst.append(num)
    return ''.join(lst[:len(lst) - k])

