
#solution1 
def solution1(s, n):
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upp.lower()
    lst = upp*2+lower*2
    ans = [" " if i == " " else lst[lst.index(i)+n] for i in list(s)]
    return "".join(ans)

#solution2 
# islower /isupper 체크해서 각 리스트에서 뽑아보기 
def solution2(s, n):
    upp = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")*2
    lower = upp.lower()*2
    ans = [" " if i == " " else upp[upp.index(i)+n] if i.isupper() else lower[lower.index(i)+n] for i in list(s)]
    return "".join(ans)

#solution3
# 문자열을 리스트에 지정하는 대신, askii로 비교?
