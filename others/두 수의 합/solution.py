
def sollution(lst,target):
    lst.sort()
    result = [0,0]
    for i in lst:
        if i > target:
            break
        if i!=target-i and target-i in lst:
            result = sorted([i,target-i])
    return result





# lst = [7, 3, 2, 13, 9, 15, 8, 11]
# target = 12 

# lst = [7, 5, 12, -9, -12, 22, -30, -35, -21]
# target = -14 

lst = [7, 5,8, 12, 20]
target = 16 

print(sollution(lst, target))