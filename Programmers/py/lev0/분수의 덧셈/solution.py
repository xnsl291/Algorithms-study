def solution(numer1, denom1, numer2, denom2):
    parent = (denom1 * denom2)
    child = (numer1*denom2 + denom1 * numer2) 
    num = parent if parent>child else child 
    
    for i in range(num,int(num/2)+1,-1):
        if parent%i == 0 and child %i==0:
            parent = int(parent/i)
            child = int(child/i)
    return child , parent  

print(solution(1,2,3,4))