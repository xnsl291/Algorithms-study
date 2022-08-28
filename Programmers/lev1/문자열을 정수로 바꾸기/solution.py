def solution(s):
    if s[0].isdigit():
        return int(s)
    else:
        return int(s[1:]) if s[0] == "+" else 0-int(s[1:])

#super simple
def sol2(s):
    return int(s)


