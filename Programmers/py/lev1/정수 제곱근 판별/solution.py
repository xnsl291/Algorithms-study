#solution1
def solution(n):
    return (n**0.5+1)**2 if int(n**0.5) == (n**0.5) else -1
  
#solution2
#use math library 

from math import sqrt
def solution(n):
    return (sqrt(n)+1)**2 if sqrt(n)%1==0 else -1

#solution3
#math library, pow function

from math import sqrt
def solution(n):
    return pow(sqrt(n)+1,2) if sqrt(n)%1==0 else -1



