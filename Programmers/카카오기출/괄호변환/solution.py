ans = []

def split_str(s):
    if len(s) == 0:
        return ""
    
    lst = [ (1 if i == "(" else -1 if i==")" else " ") for i in s]
    sum = lst[0]

    for i in range(len(lst)-1):
        sum+=lst[i+1] 
        if sum ==0 :
            index = i
            break
        
    cnt,u,v = 0,s[:i+2], s[i+2:]

    for i in lst[:i+2]: 
        cnt += i
        if lst[0] <0 or cnt<0 : 
            ans.append("".join(["(",v,")"]))
            ans.append("".join( [")" if i== "(" else "(" if i==")" else "" for i in u[1:-1] ] ))

        else:
            ans.append(u)
            split_str(v)

        break

    return "".join(ans) 
    