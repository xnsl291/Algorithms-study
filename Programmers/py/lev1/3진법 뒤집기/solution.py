def solution(n):
    result , target = 0, 3
    # lst = []
    lst = []

    # 3진법 구화기 
    while(n):
        lst.append( n%target )
        n = n//3
    # lst.append(str(n))

    # 10 진법으로 변경
    for i in range(len(lst)):
        result += (lst[i] * pow( target , len(lst)-i-1   ) )
    return result

###################################################
    ## better solution 

    ## str('숫자 혹은 문자로 이루어진 문자열',해당 진법) 
    # while n:
    #     #append
    #     lst += str(n%3)
    #     n = n//3
    ## int('숫자 혹은 문자로 이루어진 문자열',해당 진법) 
    # return int( "".join(lst), 3 )

print(solution(45))