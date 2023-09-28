import math
def solution(brown, yellow):
    
    lst = [ i for i in range(1,int(math.sqrt(yellow))+1) if yellow%i==0]
    
    for i in lst:
        w ,h = i , yellow//i
        if (4+h*2+w*2) == brown:
            return [w+2,h+2] if w>=h else [h+2,w+2]