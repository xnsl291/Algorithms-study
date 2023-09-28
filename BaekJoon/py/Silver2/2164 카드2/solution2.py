#solution2 - queue
lst = list(range(1,int(input())+1))

while len(lst)>1:
    lst.pop(0)
    lst.append(lst[0])
    # lst.pop(0)
    
print(lst[0])