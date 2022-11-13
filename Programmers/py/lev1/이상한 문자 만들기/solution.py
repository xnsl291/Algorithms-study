def solution(s):
    ans = []
    for a in s.split(" "):
        tmp = "".join([a[l].lower() if l %2 !=0 else a[l].upper() for l in  range(len(a))])
        ans.append(tmp)
    return " ".join(ans)


#enumerate, map 이용
def solution2(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

