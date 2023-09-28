def solution(age):
    # // 97~122
    return "".join( [ chr(int(i)+97) for i in list(str(age))       ] )