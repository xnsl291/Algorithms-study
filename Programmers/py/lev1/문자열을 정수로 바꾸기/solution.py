def solution(s):
    if s[0].isdigit():
        return int(s)
    else:
        return int(s[1:]) if s[0] == "+" else 0-int(s[1:])

#super simple
def sol2(s):
    return int(s)

# another way : usage of sum & exponent
def str2int(s): 

    result = sum([ int(s[-i-1] ) *(10**i) for i in range(len(s)-1)])

    if s[0].isdigit():#부호없음
        result+= int(s[0])
    elif s[0] == "-":
        result *=-1
    return result
    