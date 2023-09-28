def solution(lst,n):
    ans =[]

    for i in range(len(lst)):
        ans.append(lst[i][n])
        print(ans)
       
    # ans.sort()
        
    return ans


lst = ["sun", "bed", "car"]
n = 1
print(solution(lst,n))