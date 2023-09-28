#solution2 - queue
#FIFO
lst = list(range(1,int(input())+1))

while len(lst)>1:
    lst.pop(0)
    lst.append(lst[0])
    lst.pop(0)
    