def solution(n):
    num = bin(n)[2:].count("1")
    while(True):
        n +=1
        if num==bin(n)[2:].count("1"):
            break

    return n

print(solution(15))