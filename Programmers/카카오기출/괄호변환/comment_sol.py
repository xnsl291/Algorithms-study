ans = []

def split_str(s):
    #빈문자열 들어올 경우
    if len(s) == 0:
        return ""
    
    lst = [ (1 if i == "(" else -1 if i==")" else " ") for i in s]
    sum = lst[0]

    #u,v 분리 
    for i in range(len(lst)-1):
        sum+=lst[i+1] 
        if sum ==0 :
            index = i
            break
        
    cnt,u,v = 0,s[:i+2], s[i+2:]

    # print("u,v ==========",u,v)

    for i in lst[:i+2]:  # u 판별
        cnt += i

        # u가 올바르지 않은, v가 올바른 --> )로시작 or ()) 인경우 
        if lst[0] <0 or cnt<0 : #
            #case 4 실행

            # print(f"u ===={u}")
            # print(f"v ===={v}")

            # v 앞뒤로 '(' , ')' 추가
            ans.append("".join(["(",v,")"]))

            # u 문자열치환 후 추가
            ans.append("".join( [")" if i== "(" else "(" if i==")" else "" for i in u[1:-1] ] ))

            # print(f"ans = {ans}")

        else:
            ans.append(u)
            split_str(v)

        break

    return "".join(ans) 
    

# s = "()(()))("
# s = "))(()("  
s= "()))((()"   #"()(())()"
# s="(()())()"
# s = ")("

print(split_str(s))