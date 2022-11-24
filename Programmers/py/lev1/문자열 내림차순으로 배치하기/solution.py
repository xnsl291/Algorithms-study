
def solution(s):
    return "".join(sorted(s,reverse=True))

#askii 활용
# def solution(s):
#     tmp_lst = sorted([ord(i) for i in s],reverse=True)
#     return "".join([chr(i) for i in tmp_lst])


s = "Zbcdefg"
print(solution(s))