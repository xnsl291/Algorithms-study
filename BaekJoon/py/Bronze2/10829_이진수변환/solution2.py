# recursive 

lst = []
def convert(n):
    if n//2 != 1 :
        n = n//2
        lst.insert(0,str(n%2))
        convert(n)
    else:
        lst.insert(0,str(1))
        
    return "".join(lst)


n = int(input())
print(convert(n))