def solution(num):
    return 0 if num ==1 else solution(num)

def collatz(num):
    
    cnt = 0

    while (num > 1):
        num = num/2 if num%2==0 else num*3+1
        cnt+=1 
        if num==1 :
            break
        if cnt==500 :
            cnt = -1
            break

    return cnt

    