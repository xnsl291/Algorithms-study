import re
def solution(id):
    id = id.lower()
    id = re.sub(r"[^a-z0-9-_.]","",id)
    id = re.sub(r"\.+",".",id)  
    id = re.sub(r"^[.]|[.]$","",id)
    id = "a" if len(id)==0 else id[:15] 
    id = re.sub(r"[.]$","",id)
    id = id if len(id)>2 else id+ "".join([id[-1] for i in range(3-len(id))])

    return id
    

id = "...!@BaT#*..y.abcdefghijklm"
answer = "bat.y.abcdefghi"
print(solution(id)==answer)