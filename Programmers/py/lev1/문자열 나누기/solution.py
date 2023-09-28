def solution(s):
    head = s[0]
    cnt,answer = 0,0
    # tmp_str = ''
    length = len(s)-1
    
    for idx,i in enumerate(s): 
        cnt = cnt+1 if i == head else cnt-1
        # tmp_str+=i 
        
        if cnt==0 :
            answer+=1
            head= s[idx+1] if idx<length else s[idx]
            cnt = 0
        elif idx == length and cnt !=0:
            answer +=1
    return answer

# print(solution("aaabbaccccabba"))
print(solution("abracadabra"))